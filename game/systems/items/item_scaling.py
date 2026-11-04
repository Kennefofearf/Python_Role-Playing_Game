def get_item_level_multiplier(item_lvl, rarity):
    if rarity == "green":
        if item_lvl <= 5:
            return 1.0
        elif item_lvl <= 10:
            return 1.1
        elif item_lvl <= 15:
            return 1.2
        elif item_lvl <= 20:
            return 1.3
        elif item_lvl <= 25:
            return 1.4
        elif item_lvl <= 30:
            return 1.5
        elif item_lvl <= 32:
            return 1.6
        elif item_lvl <= 34:
            return 1.7
        elif item_lvl <= 36:
            return 1.8
        elif item_lvl <= 38:
            return 1.9
        elif item_lvl <= 40:
            return 2.0
        elif item_lvl <= 42:
            return 2.1
        elif item_lvl <= 44:
            return 2.2
        elif item_lvl <= 46:
            return 2.3
        elif item_lvl <= 48:
            return 2.4
        elif item_lvl <= 50:
            return 2.5
        elif item_lvl <= 52:
            return 2.6
        elif item_lvl <= 54:
            return 2.7
        elif item_lvl <= 56:
            return 2.8
        elif item_lvl <= 58:
            return 2.9
        else:
            return 3.0
    elif rarity == "blue":
        if item_lvl <= 40:
            return 1.0
        elif item_lvl <= 42:
            return 1.1
        elif item_lvl <= 44:
            return 1.2
        elif item_lvl <= 46:
            return 1.3
        elif item_lvl <= 48:
            return 1.4
        elif item_lvl <= 50:
            return 1.5
        elif item_lvl <= 52:
            return 1.6
        elif item_lvl <= 54:
            return 1.7
        elif item_lvl <= 56:
            return 1.8
        elif item_lvl <= 58:
            return 1.9
        else:
            return 2.0
    else:
        return 1.0


def get_base_ac_multiplier(item_lvl):
    if item_lvl <= 5:
        return 1.0
    elif item_lvl <= 10:
        return 1.1
    elif item_lvl <= 15:
        return 1.2
    elif item_lvl <= 20:
        return 1.3
    elif item_lvl <= 25:
        return 1.4
    elif item_lvl <= 30:
        return 1.5
    elif item_lvl <= 32:
        return 1.6
    elif item_lvl <= 34:
        return 1.7
    elif item_lvl <= 36:
        return 1.8
    elif item_lvl <= 38:
        return 1.9
    elif item_lvl <= 40:
        return 2.0
    elif item_lvl <= 42:
        return 2.1
    elif item_lvl <= 44:
        return 2.2
    elif item_lvl <= 46:
        return 2.3
    elif item_lvl <= 48:
        return 2.4
    elif item_lvl <= 50:
        return 2.5
    elif item_lvl <= 52:
        return 2.6
    elif item_lvl <= 54:
        return 2.7
    elif item_lvl <= 56:
        return 2.8
    elif item_lvl <= 58:
        return 2.9
    else:
        return 3.0


def get_base_dmg_multiplier(item_lvl):
    if item_lvl <= 5:
        return 1.0
    elif item_lvl <= 10:
        return 1.1
    elif item_lvl <= 15:
        return 1.2
    elif item_lvl <= 20:
        return 1.3
    elif item_lvl <= 25:
        return 1.4
    elif item_lvl <= 30:
        return 1.5
    elif item_lvl <= 32:
        return 1.6
    elif item_lvl <= 34:
        return 1.7
    elif item_lvl <= 36:
        return 1.8
    elif item_lvl <= 38:
        return 1.9
    elif item_lvl <= 40:
        return 2.0
    elif item_lvl <= 42:
        return 2.1
    elif item_lvl <= 44:
        return 2.2
    elif item_lvl <= 46:
        return 2.3
    elif item_lvl <= 48:
        return 2.4
    elif item_lvl <= 50:
        return 2.5
    elif item_lvl <= 52:
        return 2.6
    elif item_lvl <= 54:
        return 2.7
    elif item_lvl <= 56:
        return 2.8
    elif item_lvl <= 58:
        return 2.9
    else:
        return 3.0

