BLOCKED_CELLS = {
    # Northern Mountains
    (30, 77, 61, 38, 0, 140, 0),
    # ant colony walls
    (35, 0, 0, 0, 255, 217, 102),
    # water
    (126, 0, 0, 0, 0, 0, 255),
    # rock
    (178, 158, 158, 158, 191, 191, 191),
    # kobold village walls
    (32, 0, 0, 0, 255, 255, 255),
    # kobold village fences
    (35, 255, 255, 255, 0, 140, 0),
    (35, 255, 255, 255, 255, 204, 51),
    # gravestones
    (32, 0, 140, 0, 255, 255, 255),
    (43, 255, 255, 255, 0, 140, 0)
}


def collision_check(game_map, dy, dx, next_y, next_x):
    if not (0 <= next_y < len(game_map) and 0 <= next_x < len(game_map[next_y])):
        return 0, 0

    if game_map[next_y][next_x] in BLOCKED_CELLS:
        return 0, 0

    return dy, dx
