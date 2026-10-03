import curses
from UI.colors import RED


def create_enemy_window(stdscr):
    screen_h, screen_w = stdscr.getmaxyx()

    win_h, win_w = 6, 50

    start_y, start_x = 1, (screen_w - win_w) // 2
    target_window = curses.newwin(win_h, win_w, start_y, start_x)

    return target_window


def draw_enemy_window(enemy_window, selected):
    enemy_window.erase()
    enemy_window.box()

    win_h, win_w = enemy_window.getmaxyx()

    if selected and selected.alive:
        selected_name = f"{selected.name} [{selected.lvl}]"
        enemy_window.addstr(1, win_w // 2 - (len(selected_name) // 2), f"{selected_name}")

        hp_percent = selected.hp / selected.max_hp
        bar_width = win_w - 16
        filled = int(hp_percent * bar_width)

        hp_bar = "#" * filled + "-" * (bar_width - filled)

        hp_display = f"{selected.hp} / {selected.max_hp}"

        enemy_window.addstr(3, win_w // 2 - (len(hp_bar) // 2), f"[{hp_bar}]", curses.color_pair(RED))
        enemy_window.addstr(3, win_w // 2 - (len(hp_display) // 2), hp_display)
        enemy_window.addstr(4, win_w // 6, f"STR: {selected.st}")
        enemy_window.addstr(4, win_w - (win_w // 3), f"DEF: {selected.df}")

        enemy_window.refresh()
    else:
        enemy_window.erase()
        enemy_window.box()
        enemy_window.refresh()
