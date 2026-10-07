import curses


def title_screen(stdscr, saved_characters):

    title = f"Python Role-Playing Game"

    new_game_option = f"[A] NEW GAME"
    quit_option = f"[Q] QUIT"
    continue_option = f"[W] CONTINUE"
    map_editor = f"[M] Map Editor"

    can_continue = bool(saved_characters)

    while True:
        stdscr.clear()

        screen_y, screen_x = stdscr.getmaxyx()

        start_y, start_x = screen_y // 2, screen_x // 2

        stdscr.addstr(start_y, start_x - (len(title) // 2), title)

        row = start_y + 10

        stdscr.addstr(row, start_x - (len(new_game_option) // 2), new_game_option)
        row += 2

        if saved_characters:
            stdscr.addstr(row, start_x - (len(continue_option) // 2), continue_option)
            can_continue = True
            row += 2
        else:
            can_continue = False

        stdscr.addstr(row, start_x - (len(map_editor) // 2), map_editor)
        row += 2

        stdscr.addstr(row, start_x - (len(quit_option) // 2), quit_option)

        stdscr.refresh()

        key = stdscr.getch()

        if key == ord("a"):
            return "new_game"

        elif key == ord("w"):
            if can_continue:
                return "continue"
            else:
                continue

        elif key == ord("m"):
            return "map_editor"

        elif key == ord("q"):
            return "quit"
