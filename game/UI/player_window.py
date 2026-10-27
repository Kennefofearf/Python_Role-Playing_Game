import curses
import modules.item_module


def create_player_window(stdscr):
    screen_y, screen_x = stdscr.getmaxyx()

    playerwin_h = 10
    playerwin_w = 20

    y = (screen_y - playerwin_h) - 1
    x = 1

    player_window = curses.newwin(playerwin_h, playerwin_w, y, x)

    return player_window


def create_gear_progress_window(stdscr):
    screen_y, screen_x = stdscr.getmaxyx()

    playerwin_h = 10
    playerwin_w = 20

    y = (screen_y - playerwin_h) - 1
    x = (screen_x - playerwin_w) - 1

    gear_progress_window = curses.newwin(playerwin_h, playerwin_w, y, x)

    return gear_progress_window


def draw_player_window(player_window, player):
    player_window.erase()
    player_window.box()

    player_window.addstr(1, 2, f"{player.name}  Lvl: {player.lvl}")

    if player.weapon:
        player_window.addstr(3, 1, f"DMG: {player.weapon.min_dmg + player.st} - "
                                   f"{player.weapon.max_dmg + player.st}")
    else:
        player_window.addstr(3, 1, f"DMG: {player.st} - {player.st}")

    player_window.addstr(4, 1, f" HP:   {player.hp} / {player.max_hp}")
    player_window.addstr(5, 1, f"STR:   {player.st}")
    player_window.addstr(6, 1, f"DEF:   {player.df} (AC: {player.ac})")
    player_window.addstr(7, 1, f" XP: {player.total_req_xp - player.req_xp} / {player.total_req_xp}")
    player_window.addstr(8, 1, f"[")
    player_window.addstr(8, 2, f"{player.xp_bar_text:<10}")
    player_window.addstr(8, 12, f"]")
    player_window.refresh()


def draw_gear_progress_window(gear_progress_window, player, draw_ms, refresh_ms):
    gear_progress_window.erase()
    gear_progress_window.box()

    h, w = gear_progress_window.getmaxyx()

    window_title = "Gear Progress"

    gear_progress_window.addstr(1, (w // 2) - (len(window_title) // 2), window_title)
    if player.head:
        xp_percentage = player.head.get_xp_percentage()
        gear_progress_window.addstr(3, 1, f"  Head: {xp_percentage}% [{player.head.skill_points}]")
    else:
        gear_progress_window.addstr(3, 1, f"  Head: None")

    if player.chest:
        xp_percentage = player.chest.get_xp_percentage()
        gear_progress_window.addstr(4, 1, f" Chest: {xp_percentage}% [{player.chest.skill_points}]")
    else:
        gear_progress_window.addstr(4, 1, f" Chest: None")

    if player.feet:
        xp_percentage = player.feet.get_xp_percentage()
        gear_progress_window.addstr(5, 1, f"  Feet: {xp_percentage}% [{player.feet.skill_points}]")
    else:
        gear_progress_window.addstr(5, 1, f"  Feet: None")

    if player.weapon:
        xp_percentage = player.weapon.get_xp_percentage()
        gear_progress_window.addstr(6, 1, f"Weapon: {xp_percentage}% [{player.weapon.skill_points}]")
    else:
        gear_progress_window.addstr(6, 1, f"Weapon: None")

    #gear_progress_window.addstr(7, 1, f"{draw_ms:.1f}, {refresh_ms:.1f}")

    gear_progress_window.refresh()

