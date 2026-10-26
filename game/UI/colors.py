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


def get_pair_id(foreground, background, color_ids, pair_ids):
    pair_key = (foreground, background)

    if pair_key in pair_ids:
        return pair_ids[pair_key]
    else:
        foreground_id = get_color_id(foreground, color_ids)
        background_id = get_color_id(background, color_ids)

        pair_id = 21 + len(pair_ids)

        if pair_id >= curses.COLOR_PAIRS:
            raise ValueError("No more color pair slots!")

        curses.init_pair(pair_id, foreground_id, background_id)
        pair_ids[pair_key] = pair_id

        return pair_id


def get_color_id(rgb, color_ids):
    if rgb in color_ids:
        return color_ids[rgb]
    else:
        red = round(rgb[0] * 1000 / 255)
        green = round(rgb[1] * 1000 / 255)
        blue = round(rgb[2] * 1000 / 255)

        color_id = 21 + len(color_ids)

        if color_id >= curses.COLORS:
            raise ValueError("No more custom color slots!")

        curses.init_color(color_id, red, green, blue)
        color_ids[rgb] = color_id

        return color_id