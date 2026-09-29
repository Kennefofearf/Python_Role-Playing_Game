import curses


def create_combat_log_windows(stdscr):
    screen_h, screen_w = stdscr.getmaxyx()

    outer_h = 10
    outer_w = max(30, int(screen_w * 0.55))

    y = (screen_h - outer_h) - 1
    x = 22
    outer_log_window = curses.newwin(outer_h, outer_w, y, x)
    outer_log_window.refresh()

    inner_log_window = outer_log_window.derwin(outer_h - 2, outer_w - 2, 1, 1)
    inner_log_window.scrollok(True)
    inner_log_window.idlok(True)

    outer_log_window.box()

    inner_log_window.refresh()

    return outer_log_window, inner_log_window, outer_h, outer_w


def draw_log(log_win, combat_messages, scroll_offset):
    h, w = log_win.getmaxyx()
    log_win.erase()

    start = max(0, len(combat_messages) - h - scroll_offset)
    visible = combat_messages[start:start + h]

    for row, message_pair in enumerate(visible):
        col = 0
        for text, color_pair in message_pair:
            text = str(text)

            if color_pair == 0:
                log_win.addstr(row, col, text[:w-col])
            else:
                log_win.addstr(row, col, text[:w-col], curses.color_pair(color_pair))

            col += len(text)

    log_win.refresh()


def handle_scroll_log(inner, mx, my, bstate, scroll_offset, combat_messages, log_height):
    scroll_log_y, scroll_log_x = inner.getbegyx()
    scroll_log_h, scroll_log_w = inner.getmaxyx()

    wheel_up = getattr(curses, "BUTTON4_PRESSED", 65536)
    wheel_down = getattr(curses, "BUTTON5_PRESSED", 2097152)

    if scroll_log_y <= my < scroll_log_y + scroll_log_h and scroll_log_x <= mx < scroll_log_x + scroll_log_w:

        if wheel_up and (bstate & wheel_up):
            scroll_offset += 1
        elif wheel_down and (bstate & wheel_down):
            scroll_offset = max(0, scroll_offset - 1)

        max_scroll = max(0, len(combat_messages) - log_height)
        scroll_offset = min(scroll_offset, max_scroll)

    return scroll_offset


