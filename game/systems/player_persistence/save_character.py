from systems.item_persistence.save_item import item_to_dict
from systems.item_persistence.save_collected_gems import gem_to_dict


def player_to_dict(player):
    saved_char = {
        "name": player.name,
        "base_max_hp": player.base_max_hp,
        "hp": player.hp,
        "base_st": player.base_st,
        "base_df": player.base_df,
        "base_ac": player.base_ac,
        "base_mp": player.base_mp,
        "base_evasion": player.base_evasion,
        "base_crit_rate": player.base_crit_rate,
        "base_crit_dmg": player.base_crit_dmg,
        "base_hp_rr": player.base_hp_rr,
        "base_hp_ra": player.base_hp_ra,
        "req_xp": player.req_xp,
        "total_req_xp": player.total_req_xp,
        "lvl": player.lvl,
        "position": player.position,
        "inventory": [],
        "collected_gems": [],
        "ability_slots": player.ability_slots
    }

    if player.collected_gems is not None:
        saved_char["collected_gems"] = player.collected_gems
    else:
        saved_char["collected_gems"] = []

    for item in player.inventory:
        item_data = item_to_dict(item)
        saved_char["inventory"].append(item_data)

    if player.weapon is not None:
        saved_char["weapon"] = player.weapon.id
    else:
        saved_char["weapon"] = None

    if player.head is not None:
        saved_char["head"] = player.head.id
    else:
        saved_char["head"] = None

    if player.chest is not None:
        saved_char["chest"] = player.chest.id
    else:
        saved_char["chest"] = None

    if player.feet is not None:
        saved_char["feet"] = player.feet.id
    else:
        saved_char["feet"] = None

    return saved_char


