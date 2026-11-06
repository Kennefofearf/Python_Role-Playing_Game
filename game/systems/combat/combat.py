import random
from systems.items.loot_generator import roll_item_drop
from modules.item_module import Item
from modules.effect_module import ActiveStun
from UI.colors import get_rarity_color
import time


def is_adjacent(p1, p2):
    y1, x1 = p1
    y2, x2 = p2
    return abs(y1 - y2) + abs(x1 - x2) == 1


def player_auto_attack_logic(player, add_log_messages, combat_messages):
    equipment = [player.weapon, player.head, player.chest, player.feet]

    target = player.target

    if target is None:
        return

    if not target.alive:
        player.target = None
        return

    if is_adjacent(player.position, target.position):
        now = time.time()
        if now - player.last_attack_time >= player.attack_cooldown:

            if player.weapon:
                dmg = (random.randint((player.weapon.min_dmg + player.st),
                       (player.weapon.max_dmg + player.st))) - target.df
            else:
                dmg = player.st - target.df

            if player.weapon and player.weapon.has_node("parry") and player.parry_ready:
                dmg += 20
                player.parry_ready = False

            species_bonus = player.get_species_damage_bonus(target.species)
            dmg *= 1 + species_bonus

            procrastination_bonus = player.get_pro_dev_bonus()
            dmg *= 1 + procrastination_bonus

            crit_roll = random.randint(1, 100)
            is_crit = player.crit_rate >= crit_roll

            if is_crit:
                dmg *= 1 + (player.crit_dmg * 0.01)

            dmg = max(0, round(dmg))

            target.take_dmg(dmg)
            player.last_attack_time = now

            if is_crit:
                add_log_messages(combat_messages, [("+++++", 0), (f"{player.name} ", 2), ("crits ", 0), (f"{target.name} ", 1),
                                                   (f"for ", 0), (f"{dmg}", 2), ("!!!", 0), ("+++++", 0)])
            else:
                add_log_messages(combat_messages, [(f"{target.name} ", 1), ("is hit for ", 0), (f"{dmg}", 2),
                                                   ("!", 0)])

            if player.weapon:
                Item.gain_item_xp(player.weapon, 3)

        if not target.alive:
            player.xp_gain(target.xp)

            dropped_item = roll_item_drop(target)

            if dropped_item:
                if len(player.inventory) >= 20:
                    add_log_messages(combat_messages, [(f"Inventory is full.", 1)])
                else:
                    player.inventory.append(dropped_item)
                    item_color = get_rarity_color(dropped_item)
                    add_log_messages(combat_messages, [(f"Picked up: ", 0),
                                                       (f"{dropped_item.name}", item_color)])

            player.target = None


def enemy_auto_attack_logic(enemies, player, add_log_messages, combat_messages):

    for enemy in enemies:
        if not enemy.alive:
            continue

        is_stunned = any(effect.effect_id == "stun" for effect in enemy.active_effects)

        if is_stunned:
            enemy.is_attacking = False
            continue

        if is_adjacent(enemy.position, player.position):
            enemy.is_attacking = True
            now = time.time()
            if now - enemy.last_attack_time >= enemy.attack_cooldown:

                evasion_roll = random.randint(1, 100)
                player_evasion_total = player.evasion + (player.ac // 5)
                player_def_total = player.df + player.ac

                if player_evasion_total >= evasion_roll:
                    player.parry_ready = True

                    if player.feet:
                        Item.gain_item_xp(player.feet, 10)

                    if player.head:
                        Item.gain_item_xp(player.head, 3)

                    add_log_messages(combat_messages,
                                     [(f"{player.name} ", 2), ("evades the attack!", 0)])
                    enemy.last_attack_time = now
                    continue

                dmg = enemy.st - player_def_total + round(player.ac // 2)

                if dmg <= 0:
                    dmg = 0

                player.take_dmg(max(0, dmg))

                if player.chest:
                    Item.gain_item_xp(player.chest, 3)

                if player.head:
                    Item.gain_item_xp(player.head, 3)

                enemy.last_attack_time = now
                add_log_messages(combat_messages,
                                 [(f"{player.name} ", 2), ("is hit for ", 0), (f"{dmg}", 1), ("!", 0)])

        else:
            enemy.is_attacking = False
