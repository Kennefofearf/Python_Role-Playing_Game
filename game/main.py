import curses
import time
import os
from UI.title_screen import title_screen
from systems.combat.ability_logic import use_ability, update_active_effects
from curses import wrapper
from systems.combat.combat import player_auto_attack_logic, enemy_auto_attack_logic
from UI.inventory_screen import open_inventory_window
from UI.enemy_window import draw_enemy_window, create_enemy_window
from UI.player_window import \
    create_player_window, draw_player_window, create_gear_progress_window, draw_gear_progress_window
from systems.player_persistence.character_creator import create_player_character
from UI.character_select_screen import character_select_screen
from systems.player_persistence.load_charcter import load_character
from systems.player_persistence.json_to_player import json_to_player
from systems.player_persistence.get_saved_characters import get_saved_characters
from UI.colors import init_colors, RED_BG
from UI.combat_log import create_combat_log_windows, draw_log, handle_scroll_log
from UI.action_bar import create_action_bar, draw_action_bar
from UI.create_game_windows import create_game_windows
from UI.character_sheet import show_character_sheet
from UI.map_editor import map_editor
from modules.player_module import Player

from modules.monster_module import GiantAnt, AntWarrior, AntWorker, AntElite, RoyalScoutAnt, RoyalWarriorAnt, \
    RoyalGuardAnt, AntQueen, GiantSpider, Crab, KoboldScout, KoboldWorker, KoboldHunter, KoboldWarrior, KoboldElite, \
    KoboldChief, Bear, Deer, Snake, Boar, Rakarz

from modules.camera_module import Camera
from systems.player_persistence.save_character import player_to_dict
from systems.player_persistence.player_to_json import player_dict_to_json
from systems.maps.map_system import display_xp_map
from data.maps.sw_island_rules import collision_check
from systems.convert_xp_file import load_xp

filename = r"C:\Users\Kenny\PycharmProjects\ASCIIProject\game\maps\SW_Island.xp"

enemies = []

ABILITY_KEYS = {ord("1"): "1", ord("2"): "2", ord("3"): "3", ord("4"): "4"}

MIN_HEIGHT = 30
MIN_WIDTH = 120

DEFAULT_HEIGHT = 60
DEFAULT_WIDTH = 150

os.system(f"mode con: cols={DEFAULT_WIDTH} lines={DEFAULT_HEIGHT}")

for enemy in [GiantAnt, Kobold, Bear]:
    for _ in range(3):
        e = enemy()
        enemies.append(e)

for elite in [AntQueen]:
    for _ in range(1):
        e = elite()
        enemies.append(e)


def mouse_actions(mx, my, bstate, player):
    if bstate & curses.BUTTON1_CLICKED:
        for enemy in enemies:
            if (my, mx) == tuple(enemy.position) and enemy.alive:
                player.target = enemy
                return True, enemy
        return True, None
    return False, None


def draw_enemies(stdscr, enemies, selected, prev_positions, camera, start_y, start_x):
    for enemy in enemies:
        if not enemy.alive:
            continue

        screen_y, screen_x = camera.world_to_screen(enemy.position[0], enemy.position[1], start_y, start_x)

        if not (start_y <= screen_y < start_y + camera.height and start_x <= screen_x < start_x + camera.width):
            continue

        if enemy == selected:
            attr = curses.color_pair(1)
        else:
            attr = curses.A_NORMAL

        stdscr.addch(screen_y, screen_x, enemy.icon, attr)
        prev_positions.append((screen_y, screen_x))


def world_event_logic(player, py, px, stdscr, combat_messages, inner, scroll_offset, enemy_window, game_map, start_y,
                      start_x, camera):
    now = time.time()

    win_y, win_x = enemy_window.getbegyx()
    win_h, win_w = enemy_window.getmaxyx()

    player.regenerate_hp(now)
    update_active_effects(player, now, combat_messages)
    ny, nx = player.future_position(py, px)
    py, px = collision_check(game_map, py, px, ny, nx)

    if not inside_map(game_map, ny, nx):
        py, px = 0, 0
        ny, nx = player.future_position(py, px)

    player_hit = player_auto_attack_logic(player, add_log_messages, combat_messages)
    enemy_hit = enemy_auto_attack_logic(enemies, player, add_log_messages, combat_messages)

    if player_hit or enemy_hit:
        draw_log(inner, combat_messages, scroll_offset)

    if player.player_death:
        add_log_messages(combat_messages, [(f"RIP...", 1)])
        draw_log(inner, combat_messages, scroll_offset)
        screen_y, screen_x = camera.world_to_screen(player.position[0], player.position[1], start_y, start_x)
        stdscr.addstr(screen_y, screen_x, player.icon, curses.color_pair(RED_BG))
        stdscr.refresh()
        time.sleep(3)
        return True

    for e in enemies:

        update_active_effects(e, now, combat_messages)

        e.respawn_timer(player)
        if not e.alive:
            continue

        ey, ex = e.enemy_random_movement()
        ey, ex = e.aggro(player)
        ney, nex = e.future_position(ey, ex)
        ey, ex = collision_check(game_map, ey, ex, ney, nex)

        if not inside_map(game_map, ney, nex):
            ey = 0
            ex = 0

        elif (ney, nex) == tuple(player.position):
            ey = 0
            ex = 0

        elif (ny, nx) == tuple(e.position):
            py = 0
            px = 0

        elif (ny, nx) == (ney, nex):
            py = 0
            px = 0

        if not e.movement_range(ey, ex) and not e.is_aggroed:
            # if not e.is_attacking and e.return_home():
            #     ey -= e.position[0] - e.home_position[0]
            #     ex -= e.position[1] - e.home_position[1]

            ey, ex = 0, 0

        e.move(ey, ex)

    player.move(py, px)

    return False


def movement_area(win, y, x):
    h, w = win.getmaxyx()
    return 1 <= y <= h - 2 and 1 <= x <= w - 2


def inside_map(game_map, y, x):
    return (
        0 <= y < len(game_map) and 0 <= x < len(game_map[y])
    )


def add_log_messages(combat_messages, message_pair):
    if len(combat_messages) > 200:
        combat_messages.pop(0)

    combat_messages.append(message_pair)


def gamestart(stdscr, player):
    curses.cbreak()
    init_colors()

    curses.noecho()
    curses.curs_set(0)
    stdscr.keypad(True)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    curses.mouseinterval(200)
    stdscr.timeout(17)
    selected = None

    stdscr.clear()

    game_map = load_xp(filename)
    color_ids = {}
    pair_ids = {}

    player.position = [75, 21]

    # Window rendering

    stdscr.border(ord("#"), ord("#"), ord("#"), ord("#"), ord("O"), ord("O"), ord("O"), ord("O"))
    stdscr.refresh()

    player_window = create_player_window(stdscr)
    gear_progress_window = create_gear_progress_window(stdscr)
    action_bar = create_action_bar(stdscr)

    enemy_window = create_enemy_window(stdscr)

    prev_positions = []

    outer, inner, outer_h, outer_w = create_combat_log_windows(stdscr)
    combat_messages = []
    log_height = inner.getmaxyx()[0]
    scroll_offset = 0
    window_too_small = False

    last_y, last_x = stdscr.getmaxyx()
    start_y = last_y // 8
    world_height = start_y + (start_y * 4) + 4
    world_width = 70 - 1 - 1
    start_x = (last_x - world_width) // 2
    camera = Camera(world_height, world_width)

    render_cache = {}

    last_view = None
    redraw_map = True

    draw_ms = 0.0
    refresh_ms = 0.0

    while True:
        y_max, x_max = stdscr.getmaxyx()

        if y_max < MIN_HEIGHT or x_max < MIN_WIDTH:
            window_too_small = True

            stdscr.clear()
            stdscr.addstr(0, 0, "Expand window to continue")
            stdscr.refresh()
            stdscr.getch()
            continue

        if (y_max, x_max) != (last_y, last_x) or window_too_small:
            (
                enemy_window,
                outer,
                inner,
                outer_h,
                outer_w,
                player_window,
                gear_progress_window,
                action_bar,
                log_height
            ) = create_game_windows(stdscr)

            redraw_map = True
            last_y, last_x = y_max, x_max
            window_too_small = False

        camera.follow(player.position[0], player.position[1], len(game_map), len(game_map[0]))

        current_view = (camera.y, camera.x, camera.height, camera.width, start_y, start_x)

        if redraw_map or current_view != last_view:
            draw_start = time.perf_counter()
            display_xp_map(stdscr, game_map, start_y, start_x, color_ids, pair_ids, render_cache, camera)
            draw_ms = (time.perf_counter() - draw_start) * 1000

        else:
            for screen_y, screen_x in prev_positions:
                map_y = screen_y - start_y + camera.y
                map_x = screen_x - start_x + camera.x

                if (
                        start_y <= screen_y < start_y + camera.height
                        and start_x <= screen_x < start_x + camera.width
                        and 0 <= map_y < len(game_map) and 0 <= map_x < len(game_map[map_y])
                ):
                    cell = game_map[map_y][map_x]
                    char, color = render_cache[cell]
                    stdscr.addstr(screen_y, screen_x, char, color)

        prev_positions = []
        last_view = current_view
        redraw_map = False

        draw_player_window(player_window, player)
        draw_gear_progress_window(gear_progress_window, player, draw_ms, refresh_ms)
        draw_action_bar(action_bar, player)

        draw_enemy_window(enemy_window, selected)

        player.player_spawn(stdscr, prev_positions, camera, start_y, start_x)
        draw_enemies(stdscr, enemies, selected, prev_positions, camera, start_y, start_x)

        refresh_start = time.perf_counter()
        stdscr.refresh()
        refresh_ms = (time.perf_counter() - refresh_start) * 1000

        key = stdscr.getch()

        if key in (ord("w"), ord("a"), ord("s"), ord("d")):
            curses.flushinp()

        if key == ord("q"):

            data = player_to_dict(player)
            player_dict_to_json(data)

            break

        # elif key == ord("e"):
        #     stdscr.clear()
        #     map_editor(stdscr, map_1)

        elif key == ord("i"):
            player_window.clear()
            open_inventory_window(stdscr, player)
            stdscr.touchwin()
            redraw_map = True

        elif key == ord("c"):
            player_window.clear()
            show_character_sheet(stdscr, player)
            redraw_map = True

        # elif key == curses.KEY_RESIZE:
        #     create_game_windows(stdscr)

        elif key == curses.KEY_MOUSE:
            _, mx, my, _, bstate, = curses.getmouse()

            if start_y <= my < start_y + camera.height and start_x <= mx < start_x + camera.width:
                map_y = my - start_y + camera.y
                map_x = mx - start_x + camera.x

            clicked, picked = mouse_actions(map_x, map_y, bstate, player)
            selected = picked
            player.target = picked

            scroll_offset = handle_scroll_log(inner, mx, my, bstate, scroll_offset, combat_messages, log_height)

        if key in ABILITY_KEYS:
            slot = ABILITY_KEYS[key]
            ability_id = player.ability_slots[slot]

            if ability_id:
                success, message = use_ability(player, player.target, ability_id, time.time(), combat_messages)

                if not success:
                    add_log_messages(combat_messages, [(message, 0)])

        draw_log(inner, combat_messages, scroll_offset)

        py, px = player.input_action(key)

        player_died = world_event_logic(player, py, px, stdscr, combat_messages, inner, scroll_offset, enemy_window,
                                        game_map, start_y, start_x, camera)

        if player_died:
            return

        if selected and not selected.alive:
            selected = None

        stdscr.refresh()


def main(stdscr):
    while True:
        saved_characters = get_saved_characters()
        choice = title_screen(stdscr, saved_characters)

        if choice == "new_game":
            player_name = create_player_character(stdscr)
            player = Player(player_name)
            gamestart(stdscr, player)

        elif choice == "continue":
            name = character_select_screen(stdscr, saved_characters)
            data = load_character(name)
            player = json_to_player(data)
            gamestart(stdscr, player)

        elif choice == "map_editor":
            game_map = load_xp(filename)
            map_editor(stdscr, game_map)

        elif choice == "quit":
            return


wrapper(main)


