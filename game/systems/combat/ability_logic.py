from data.weapons_abilities_data import COMMON_WEAPON_ABILITIES
from modules.effect_module import DamageEffect, DotEffect, StunEffect, ActiveDot


def rebuild_abilities(unit):
    usable = set()

    if unit.weapon:
        for ability_id in unit.weapon.get("abilities", []):
            usable.add(ability_id)

    for ability_id in unit.unlocked_abilties:
        usable.add(ability_id)

    unit.abilities = list(usable)


def can_use_ability(user, ability_id, now):
    if not user.weapon:
        return False, "Required weapon not equipped..."

    if ability_id not in user.weapon.unlocked_abilities:
            return False, "Required weapon not equipped..."

    if ability_id not in user.ability_slots.values():
        return False, "Ability not equipped..."

    if ability_id in user.cooldowns and now < user.cooldowns[ability_id]:
        return False, "That ability is on cooldown."

    return True, ""


def in_range(user, target, ability_data):
    uy, ux = user.position
    ty, tx = target.position
    dist = abs(uy - ty) + abs(ux - tx)
    return dist <= ability_data.range


def update_active_effects(unit, now, combat_messages=None):
    for effect in unit.active_effects[:]:
        if now >= effect.expires_at:
            unit.active_effects.remove(effect)
            continue

        if isinstance(effect, ActiveDot):
            if now >= effect.next_tick:
                dmg = effect.damage
                unit.take_dmg(dmg)

                if combat_messages is not None and unit.alive:
                    combat_messages.append([(f"{unit.name} ", 1), (f"{effect.verb} ", 0), (f"{effect.damage} ", 2),
                                            ("damage.", 0)])

                    effect.next_tick += effect.interval


def use_ability(user, target, ability_id, now, combat_messages=None):
    ability = COMMON_WEAPON_ABILITIES[ability_id]

    ok, reason = can_use_ability(user, ability_id, now)
    if not ok:
        return False, reason

    if ability.target_type == "enemy":
        if target is None or not target.alive:
            if combat_messages is not None:
                combat_messages.append([("Invalid target.", 2)])
            return False, "Invalid target."

        if not in_range(user, target, ability):
            if combat_messages is not None:
                combat_messages.append([("Target out of range.", 2)])
            return False, "Target out of range."

    for effect in ability.effects:
        result = effect.apply(user, target, now)

        if combat_messages is not None:

            if isinstance(effect, DamageEffect):
                combat_messages.append([(f"{user.name} ", 2), ("uses ", 0), (f"{ability.name} ", 2), ("on ", 0),
                                        (f"{target.name} ", 1), ("for ", 0), (f"{result} ", 2), ("damage!", 0)])

            elif isinstance(effect, DotEffect):
                combat_messages.append([(f"{target.name} ", 1), ("starts bleeding!", 0)])

            elif isinstance(effect, StunEffect):
                combat_messages.append([(f"{target.name} ", 1), ("is stunned!", 0)])

    user.cooldowns[ability_id] = now + ability.cooldown

    return True, "ok"

