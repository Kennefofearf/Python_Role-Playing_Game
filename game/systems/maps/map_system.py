from data.maps import TEST_MAP


def display_map(stdscr, map, start_y, start_x):

    for y, row in enumerate(map):
        for x, char in enumerate(row):
            stdscr.addch(start_y + y, start_x + x, char)


def edit_map(map):
    editable_map = [list(row) for row in map]

    editable_map[1][2] = "#"

    return editable_map
