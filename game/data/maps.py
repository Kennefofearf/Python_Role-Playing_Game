TEST_MAP = [
    "##########",
    "#        #",
    "#  ###   #",
    "#   #    #",
    "#        #",
    "##########",
]


def display_map(stdscr, player, map, start_y, start_x):

    for y, row in enumerate(map):
        for x, char in enumerate(row):
            stdscr.addch(start_y + y, start_x + x, char)


