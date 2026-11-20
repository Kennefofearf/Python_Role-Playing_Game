from modules.player_module import Player
from systems.item_persistence.item_dict_to_item import item_dict_to_item


def json_to_player(data):
    player = Player(data['name'])

    player.base_max_hp = data["base_max_hp"]
    player.hp = data["hp"]
    player.base_st = data["base_st"]
    player.base_df = data["base_df"]
    player.base_ac = data["base_ac"]
    player.base_mp = data["base_mp"]
    player.base_evasion = data["base_evasion"]
    player.base_crit_rate = data["base_crit_rate"]
    player.base_crit_dmg = data["base_crit_dmg"]
    player.base_hp_rr = data["base_hp_rr"]
    player.base_hp_ra = data["base_hp_ra"]

    player.req_xp = data["req_xp"]
    player.total_req_xp = data["total_req_xp"]
    player.lvl = data["lvl"]
    player.position = data["position"]
    player.inventory = []
    player.collected_gems = data["collected_gems"]
    player.ability_slots = data["ability_slots"]
    player.weapon = None
    player.head = None
    player.chest = None
    player.feet = None

    for item_data in data["inventory"]:
        item = item_dict_to_item(item_data)
        player.inventory.append(item)

    for item in player.inventory:
        if item.id == data["weapon"]:
            player.weapon = item

        if item.id == data["head"]:
            player.head = item

        if item.id == data["chest"]:
            player.chest = item

        if item.id == data["feet"]:
            player.feet = item

    return player
