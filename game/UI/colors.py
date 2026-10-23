import curses

RED = 1
YELLOW = 2
GREEN = 3
BLUE = 4
MAGENTA = 5
UNAVAILABLE = 6
RED_BG = 7
GRAY = 8
BB = 9


def init_colors():
    curses.start_color()

    curses.init_color(20, 200, 600, 350)

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(9, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(20, 20, curses.COLOR_BLACK)

    curses.init_pair(UNAVAILABLE, GRAY, curses.COLOR_BLACK)


def get_rarity_color(item):
    return get_color_from_rarity(item.rarity)


def get_color_from_rarity(rarity):
    if rarity == "white":
        return 0
    elif rarity == "green":
        return 3
    elif rarity == "blue":
        return 4
    elif rarity == "yellow":
        return 2
    elif rarity == "purple":
        return 5