import curses
from data.cp437 import cp437_to_unicode


def main(stdscr):
    curses.curs_set(0)

    while True:
        stdscr.erase()

        stdscr.addstr(0, 0, "REXPaint CP437 Character Test")

        for code in range(256):
            row = code // 16
            col = code % 16

            y = row + 3
            x = col * 4

            char = cp437_to_unicode(code)

            stdscr.addstr(y, x, char)

        stdscr.refresh()

        key = stdscr.getch()

        if key in (ord("q"), ord("Q")):
            break

curses.wrapper(main)

if __name__ == "__main__":
    pass
