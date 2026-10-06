from data.maps import TEST_MAP
from pathlib import Path


def display_map(stdscr, map, start_y, start_x):

    for y, row in enumerate(map):
        for x, char in enumerate(row):
            stdscr.addch(start_y + y, start_x + x, char)


def edit_map(map):
    editable_map = [list(row) for row in map]

    editable_map[1][2] = "#"

    return editable_map


def save_map(game_map, filename):

    save_dir = Path(__file__).resolve().parents[2] / "maps"

    save_dir.mkdir(parents=True ,exist_ok=True)

    save_file = save_dir / filename

    with open(save_file, "w", encoding="utf-8") as file:

        for row in game_map:
            file.write("".join(row) + "\n")
