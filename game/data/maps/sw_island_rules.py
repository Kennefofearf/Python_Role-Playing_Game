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


def ant_colony_random_spawn():
    rand_mon = random.randint(0, 4)

    if rand_mon <= 1:
        return "ga"
    elif rand_mon <= 3:
        return "awk"
    else:
        return "ae"


def forest_random_spawn():
    rand_mon = random.randint(0, 9)

    if rand_mon <= 1:
        return "ks"
    elif rand_mon <= 2:
        return "kh"
    elif rand_mon <= 3:
        return "gs"
    elif rand_mon <= 4:
        return "be"
    elif rand_mon <= 5:
        return "bo"
    elif rand_mon <= 6:
        return "s"
    else:
        return "d"


def village_random_spawn():
    rand_mon = random.randint(0, 6)

    if rand_mon <= 1:
        return "ks"
    elif rand_mon <= 2:
        return "kh"
    elif rand_mon <= 3:
        return "kwr"
    else:
        return "kwk"


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
        (grasslands_random_spawn(), 39, 64, 10, 6),
        (grasslands_random_spawn(), 28, 41, 10, 6),
        (grasslands_random_spawn(), 14, 10, 10, 6),

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
        ("ga", 4, 311, 3, 3),
        ("ga", 25, 313, 3, 3),
        ("ga", 43, 309, 3, 3),
        # Ant Elites at entrance
        ("ae", 51, 289, 0, 2),
        ("ae", 51, 292, 0, 2),
        ########################
        ("ga", 73, 260, 3, 3),
        ("ga", 100, 285, 3, 3),
        ("ga", 104, 239, 3, 3),
        ("ga", 49, 310, 3, 3),
        ("ga", 66, 318, 3, 3),

        # Ant Colony (Maze)
        (ant_colony_random_spawn(), 40, 290, 20, 2),
        (ant_colony_random_spawn(), 43, 277, 20, 2),
        (ant_colony_random_spawn(), 39, 304, 20, 2),
        (ant_colony_random_spawn(), 29, 300, 20, 2),
        (ant_colony_random_spawn(), 23, 285, 20, 2),
        (ant_colony_random_spawn(), 16, 296, 20, 2),
        (ant_colony_random_spawn(), 7, 302, 20, 2),
        (ant_colony_random_spawn(), 8, 285, 20, 2),
        (ant_colony_random_spawn(), 27, 272, 20, 2),
        (ant_colony_random_spawn(), 13, 296, 20, 2),
        (ant_colony_random_spawn(), 14, 281, 20, 2),
        (ant_colony_random_spawn(), 11, 271, 20, 2),
        (ant_colony_random_spawn(), 24, 270, 20, 2),
        (ant_colony_random_spawn(), 36, 270, 20, 2),
        (ant_colony_random_spawn(), 32, 260, 20, 2),
        (ant_colony_random_spawn(), 42, 257, 20, 2),
        (ant_colony_random_spawn(), 24, 255, 20, 2),
        (ant_colony_random_spawn(), 11, 264, 20, 2),
        (ant_colony_random_spawn(), 8, 256, 20, 2),
        (ant_colony_random_spawn(), 22, 252, 20, 2),
        (ant_colony_random_spawn(), 39, 252, 20, 2),
        (ant_colony_random_spawn(), 33, 245, 20, 2),
        (ant_colony_random_spawn(), 21, 247, 20, 2),
        (ant_colony_random_spawn(), 2, 246, 20, 2),
        (ant_colony_random_spawn(), 4, 225, 20, 2),
        (ant_colony_random_spawn(), 16, 230, 20, 2),
        (ant_colony_random_spawn(), 24, 232, 20, 2),
        (ant_colony_random_spawn(), 31, 235, 20, 2),
        (ant_colony_random_spawn(), 44, 237, 20, 2),
        (ant_colony_random_spawn(), 41, 228, 20, 2),
        (ant_colony_random_spawn(), 35, 218, 20, 2),
        (ant_colony_random_spawn(), 41, 218, 20, 2),
        (ant_colony_random_spawn(), 48, 226, 20, 2),
        (ant_colony_random_spawn(), 46, 212, 20, 2),
        (ant_colony_random_spawn(), 39, 207, 20, 2),
        (ant_colony_random_spawn(), 37, 212, 20, 2),
        (ant_colony_random_spawn(), 31, 219, 20, 2),
        (ant_colony_random_spawn(), 25, 220, 20, 2),
        (ant_colony_random_spawn(), 14, 217, 20, 2),
        (ant_colony_random_spawn(), 2, 222, 20, 2),
        (ant_colony_random_spawn(), 13, 227, 20, 2),
        (ant_colony_random_spawn(), 3, 235, 20, 2),
        (ant_colony_random_spawn(), 9, 231, 20, 2),
        (ant_colony_random_spawn(), 8, 244, 20, 2),
        (ant_colony_random_spawn(), 22, 210, 20, 2),
        (ant_colony_random_spawn(), 9, 211, 20, 2),
        (ant_colony_random_spawn(), 2, 208, 20, 2),
        # Ant Colony (Long Section)
        ("ae", 2, 204, 0, 2),
        (ant_colony_random_spawn(), 15, 205, 20, 2),
        (ant_colony_random_spawn(), 34, 204, 20, 2),
        ("ae", 48, 201, 0, 2),
        (ant_colony_random_spawn(), 26, 202, 20, 2),
        (ant_colony_random_spawn(), 6, 201, 20, 2),
        ("ae", 2, 198, 0, 2),
        (ant_colony_random_spawn(), 11, 199, 20, 2),
        (ant_colony_random_spawn(), 23, 198, 20, 2),
        (ant_colony_random_spawn(), 39, 199, 20, 2),
        ("ae", 48, 199, 0, 2),
        (ant_colony_random_spawn(), 47, 186, 20, 2),
        (ant_colony_random_spawn(), 44, 186, 20, 2),
        (ant_colony_random_spawn(), 41, 186, 20, 2),
        (ant_colony_random_spawn(), 38, 186, 20, 2),
        (ant_colony_random_spawn(), 35, 186, 20, 2),
        (ant_colony_random_spawn(), 32, 186, 20, 2),
        (ant_colony_random_spawn(), 18, 196, 20, 2),
        (ant_colony_random_spawn(), 10, 192, 20, 2),
        (ant_colony_random_spawn(), 29, 186, 20, 2),
        (ant_colony_random_spawn(), 23, 190, 20, 2),
        ("ae", 21, 190,  0, 2),
        ("ae", 2, 186, 0, 2),
        ("ae", 18, 172, 0, 2),
        (ant_colony_random_spawn(), 9, 184, 20, 2),
        (ant_colony_random_spawn(), 6, 177, 20, 2),
        ("ae", 10, 177, 0, 2),
        ("ae", 10, 178, 0, 2),
        ("ae", 24, 174, 0, 2),
        (ant_colony_random_spawn(), 5, 175, 20, 2),
        (ant_colony_random_spawn(), 15, 172, 20, 2),
        ("ae", 26, 175, 0, 2),
        (ant_colony_random_spawn(), 48, 173, 20, 2),
        ("ae", 29, 168, 0, 2),
        (ant_colony_random_spawn(), 48, 169, 20, 2),
        (ant_colony_random_spawn(), 20, 169, 20, 2),
        (ant_colony_random_spawn(), 9, 165, 20, 2),
        (ant_colony_random_spawn(), 32, 166, 20, 2),
        (ant_colony_random_spawn(), 48, 163, 20, 2),
        (ant_colony_random_spawn(), 22, 162, 20, 2),
        (ant_colony_random_spawn(), 22, 160, 20, 2),
        (ant_colony_random_spawn(), 48, 156, 20, 2),
        ("ae", 47, 149, 0, 2),
        (ant_colony_random_spawn(), 18, 157, 20, 2),
        (ant_colony_random_spawn(), 8, 149, 20, 2),
        (ant_colony_random_spawn(), 17, 148, 20, 2),
        (ant_colony_random_spawn(), 23, 154, 20, 2),
        ("ae", 20, 143, 0, 2),
        ("ae", 21, 143, 0, 2),

        # Forest
        (forest_random_spawn(), 13, 346, 10, 6),
        (forest_random_spawn(), 40, 340, 10, 6),
        (forest_random_spawn(), 49, 368, 10, 6),
        (forest_random_spawn(), 15, 366, 10, 6),
        (forest_random_spawn(), 27, 398, 10, 6),
        (forest_random_spawn(), 4, 395, 10, 6),
        (forest_random_spawn(), 48, 378, 10, 6),
        (forest_random_spawn(), 48, 416, 10, 6),
        (forest_random_spawn(), 14, 462, 10, 6),
        (forest_random_spawn(), 22, 433, 10, 6),
        (forest_random_spawn(), 51, 448, 10, 6),
        (forest_random_spawn(), 9, 490, 10, 6),
        (forest_random_spawn(), 39, 489, 10, 6),
        (forest_random_spawn(), 49, 517, 10, 6),
        (forest_random_spawn(), 12, 516, 10, 6),
        (forest_random_spawn(), 55, 545, 10, 6),
        (forest_random_spawn(), 76, 606, 10, 6),
        (forest_random_spawn(), 89, 497, 10, 6),
        (forest_random_spawn(), 107, 463, 10, 6),
        (forest_random_spawn(), 154, 492, 10, 6),
        (forest_random_spawn(), 174, 502, 10, 6),

        # Road near village
        ("ks", 222, 425, 10, 6),
        ("kwk", 242, 436, 10, 6),
        ("ks", 227, 364, 10, 6),

        # Village
        (village_random_spawn(), 236, 543, 10, 6),
        (village_random_spawn(), 213, 516, 10, 6),
        (village_random_spawn(), 198, 513, 10, 6),
        (village_random_spawn(), 190, 523, 10, 6),
        (village_random_spawn(), 170, 532, 10, 6),
        (village_random_spawn(), 141, 547, 10, 6),
        (village_random_spawn(), 108, 586, 10, 6),
        (village_random_spawn(),105, 555, 10, 6),
        (village_random_spawn(), 101, 585, 10, 6),
        (village_random_spawn(), 108, 586, 10, 6),
        (village_random_spawn(), 131, 570, 10, 6),
        (village_random_spawn(), 106, 602, 10, 6),
        (village_random_spawn(), 134, 609, 10, 6),
        (village_random_spawn(), 122, 625, 10, 6),
        ("ke", 102, 624, 0, 2),
        (village_random_spawn(), 110, 629, 10, 6),
        (village_random_spawn(), 150, 668, 10, 6),
        (village_random_spawn(), 173, 642, 10, 6),
        (village_random_spawn(), 190, 659, 15, 6),
        ("ke", 173, 623, 0, 2),
        ("ke", 173, 621, 0, 2),
        (village_random_spawn(), 186, 606, 10, 6),
        (village_random_spawn(), 224, 641, 10, 6),
        (village_random_spawn(), 197, 667, 10, 6),
        ("ke", 196, 645, 0, 18),
        ("ke", 211, 640, 0, 18),
        ("ke", 195, 635, 0, 18),
        ("ke", 204, 632, 0, 2),
        (village_random_spawn(), 198, 599, 10, 6),
        (village_random_spawn(), 212, 604, 10, 6),
        (village_random_spawn(), 209, 590, 10, 6),
        (village_random_spawn(), 205, 597, 10, 6),
        (village_random_spawn(), 208, 580, 10, 6),
        (village_random_spawn(), 212, 562, 10, 6),
        (village_random_spawn(), 230, 579, 10, 6),
        ("ke", 192, 559, 0, 18),
        ("ke", 192, 572, 0, 18),

        #Kobold Chief's Home

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
