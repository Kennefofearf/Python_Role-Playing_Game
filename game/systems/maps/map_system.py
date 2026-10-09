from data.maps import TEST_MAP
from pathlib import Path


def display_map(stdscr, game_map, start_y, start_x, camera=None):
    top = camera.y if camera else 0
    left = camera.x if camera else 0

    bottom = min(len(game_map), top + camera.height) if camera else len(game_map)

    for y in range(top, bottom):
        right = min(len(game_map[y]), left + camera.width) if camera else len(game_map[y])

        for x in range(left, right):
            stdscr.addch(start_y + y - top, start_x + x - left, game_map[y][x])


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
