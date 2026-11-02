import random

from modules.monster_module import GiantAnt, AntWarrior, AntWorker, AntElite, RoyalScoutAnt, RoyalWarriorAnt, \
    RoyalGuardAnt, AntQueen, GiantSpider, Crab, KoboldScout, KoboldWorker, KoboldHunter, KoboldWarrior, KoboldElite, \
    KoboldChief, Bear, Deer, Snake, Boar, Rakarz


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

ENEMY_TYPES = {
    # Ants
    "ga": GiantAnt,
    "awr": AntWarrior,
    "awk": AntWorker,
    "ae": AntElite,
    "rsa": RoyalScoutAnt,
    "rwa": RoyalWarriorAnt,
    "rga": RoyalGuardAnt,
    # Kobolds
    "ks": KoboldScout,
    "kwk": KoboldWorker,
    "kh": KoboldHunter,
    "kwr": KoboldWarrior,
    "ke": KoboldElite,
    # Field Enemies
    "gs": GiantSpider,
    "c": Crab,
    "be": Bear,
    "d": Deer,
    "s": Snake,
    "bo": Boar,
    # Bosses
    "aq": AntQueen,
    "kc": KoboldChief,
    "rkz": Rakarz
}


def grasslands_random_spawn():
    rand_mon = random.randint(0, 9)

    if rand_mon <= 2:
        return "ga"
    elif rand_mon <= 5:
        return "bo"
    elif rand_mon == 6:
        return "ks"
    elif rand_mon == 7:
        return "s"
    elif rand_mon == 8:
        return "d"
    else:
        return "be"


def get_enemy_spawns():
    return [

        # (ENEMY_TYPE, y, x, radius, aggro_range)

        # Beaches
        ("c", 55, 17, 3, 2),
        ("c", 142, 44, 3, 2),
        # Grasslands
        (grasslands_random_spawn(), 90, 60, 10, 6),
        (grasslands_random_spawn(), 62, 83, 10, 6),
        (grasslands_random_spawn(), 59, 119, 10, 6),
        (grasslands_random_spawn(), 81, 133, 10, 6),
        (grasslands_random_spawn(), 87, 106, 10, 6),
        (grasslands_random_spawn(), 50, 345, 10, 6),
        (grasslands_random_spawn(), 85, 352, 10, 6),
        (grasslands_random_spawn(), 102, 320, 10, 6),
        (grasslands_random_spawn(), 127, 347, 10, 6),
        (grasslands_random_spawn(), 146, 320, 10, 6),
        (grasslands_random_spawn(), 134, 271, 10, 6),
        (grasslands_random_spawn(), 114, 289, 10, 6),
        (grasslands_random_spawn(), 160, 287, 10, 6),
        (grasslands_random_spawn(), 191, 235, 10, 6),
        (grasslands_random_spawn(), 154, 149, 10, 6),
        (grasslands_random_spawn(), 146, 121, 10, 6),
        (grasslands_random_spawn(), 140, 95, 10, 6),
        (grasslands_random_spawn(), 158, 106, 10, 6),
        (grasslands_random_spawn(), 106, 97, 10, 6),
        (grasslands_random_spawn(), 123, 55, 10, 6),
        (grasslands_random_spawn(), 190, 82, 10, 6),
        (grasslands_random_spawn(), 182, 135, 10, 6),
        (grasslands_random_spawn(), 213, 117, 10, 6),
        (grasslands_random_spawn(), 176, 194, 10, 6),
        (grasslands_random_spawn(), 215, 177, 10, 6),
        (grasslands_random_spawn(), 175, 270, 10, 6),
        (grasslands_random_spawn(), 132, 321, 10, 6),
        (grasslands_random_spawn(), 108, 345, 10, 6),
        (grasslands_random_spawn(), 346, 323, 10, 6),
        (grasslands_random_spawn(), 359, 362, 10, 6),
        (grasslands_random_spawn(), 371, 278, 10, 6),
        (grasslands_random_spawn(), 377, 245, 10, 6),
        (grasslands_random_spawn(), 358, 259, 10, 6),
        (grasslands_random_spawn(), 342, 279, 10, 6),
        (grasslands_random_spawn(), 359, 192, 10, 6),
        (grasslands_random_spawn(), 384, 215, 10, 6),
        (grasslands_random_spawn(), 353, 228, 10, 6),
        (grasslands_random_spawn(), 313, 179, 10, 6),
        (grasslands_random_spawn(), 337, 153, 10, 6),
        (grasslands_random_spawn(), 298, 148, 10, 6),
        (grasslands_random_spawn(), 293, 122, 10, 6),
        (grasslands_random_spawn(), 261, 113, 10, 6),
        (grasslands_random_spawn(), 215, 104, 10, 6),
        (grasslands_random_spawn(), 83, 79, 10, 6),
        (grasslands_random_spawn(), 114, 53, 10, 6),
        # Perimeter of the Ant Colony
        ("ga", 71, 84, 3, 3),
        ("ga", 101, 96, 3, 3),
        ("ga", 62, 145, 3, 3),
        ("ga", 53, 156, 3, 3),
        ("ga", 56, 175, 3, 3),
        ("ga", 83, 141, 3, 3),
        ("ga", 102, 181, 3, 3),
        ("ga", 55, 202, 3, 3),
        ("ga", 66, 234, 3, 3),
        ("ga", 86, 213, 3, 3),
        ("ga", 97, 238, 3, 3),
        ("ga", 54, 246, 3, 3),
        ("ga", 55, 271, 3, 3),
        # Ant Elites at entrance
        ("ae", 51, 289, 0, 2),
        ("ae", 51, 292, 0, 2),
        ########################
        ("ga", 73, 260, 3, 3),
        ("ga", 100, 285, 3, 3),
        ("ga", 104, 239, 3, 3),
        ("ga", 49, 310, 3, 3),
        ("ga", 66, 318, 3, 3),
        # Boss Spawns
        # Rakarz
        ("rkz", 287, 311, 800, 10)
    ]


def collision_check(game_map, dy, dx, next_y, next_x):
    if not (0 <= next_y < len(game_map) and 0 <= next_x < len(game_map[next_y])):
        return 0, 0

    if game_map[next_y][next_x] in BLOCKED_CELLS:
        return 0, 0

    return dy, dx
