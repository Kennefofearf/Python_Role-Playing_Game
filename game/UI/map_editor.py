from systems.maps.map_system import display_map


def map_editor(stdscr, game_map):
    cursor_y, cursor_x = 1, 1

    while True:

        stdscr.clear()

        screen_y, screen_x = stdscr.getmaxyx()

        display_map(stdscr, game_map, cursor_y, cursor_x)

        game_map[cursor_y][cursor_x] = "_"

        stdscr.refresh()

        key = stdscr.getch()

        if key == ord("q"):
            stdscr.clear()
            stdscr.refresh()
            break
