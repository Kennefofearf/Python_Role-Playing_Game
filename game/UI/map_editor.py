import curses
from systems.maps.map_system import display_map, save_map


def map_editor(stdscr, game_map):
    cursor_y, cursor_x = 1, 1

    while True:

        stdscr.clear()

        screen_y, screen_x = stdscr.getmaxyx()

        display_map(stdscr, game_map, 1, 1)

        stdscr.addch(1 + cursor_y, 1 + cursor_x, game_map[cursor_y][cursor_x], curses.A_REVERSE)

        stdscr.refresh()

        key = stdscr.getch()

        if key == ord("q"):
            stdscr.clear()
            stdscr.refresh()
            break

        if key == ord("w"):
            cursor_y = max(0, cursor_y - 1)

        elif key == ord("a"):
            cursor_x = min(len(game_map), cursor_x - 1)

        elif key == ord("s"):
            cursor_y = min(len(game_map) - 1, cursor_y + 1)

        elif key == ord("d"):
            cursor_x = min(len(game_map[cursor_y]) - 1, cursor_x + 1)

        elif key == ord("p"):
            save_map(game_map, "map_1.txt")

        elif key == ord("1"):
            game_map[cursor_y][cursor_x] = "#"

        elif key == ord("2"):
            game_map[cursor_y][cursor_x] = " "

        stdscr.refresh()
