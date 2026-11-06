class DamageEffect:

    def __init__(self, base_dmg, scaling_stat, scaling, dmg_type):
        self.base_dmg = base_dmg
        self.scaling_stat = scaling_stat
        self.scaling = scaling
        self.dmg_type = dmg_type

    def apply(self, user, target, now):
        stat_value = getattr(user, self.scaling_stat, 0)

        total_dmg = self.base_dmg + (stat_value * self.scaling)
        total_dmg = round(total_dmg)

        if self.dmg_type == "blunt":
            total_dmg = max(0, total_dmg - target.df)

        target.take_dmg(total_dmg)

        return total_dmg


class ActiveDot:
    def __init__(self, effect_id, name, verb, damage, interval, duration, source, now):
        self.effect_id = effect_id
        self.name = name
        self.verb = verb
        self.damage = damage
        self.interval = interval
        self.expires_at = now + duration
        self.next_tick = now + interval
        self.source = source


class DotEffect:
    def __init__(self, effect_id, name, verb, damage, interval, duration):
        self.effect_id = effect_id
        self.name = name
        self.verb = verb
        self.damage = damage
        self.interval = interval
        self.duration = duration

    def apply(self, user, target, now):
        active_dot = ActiveDot(
            effect_id=self.effect_id,
            name=self.name,
            verb=self.verb,
            damage=self.damage,
            interval=self.interval,
            duration=self.duration,
            source=user,
            now=now
        )

        target.active_effects.append(active_dot)

        return active_dot


class ActiveStun:
    def __init__(self, effect_id, name, duration, source, now):
        self.effect_id = effect_id
        self.name = name
        self.expires_at = now + duration
        self.source = source


class StunEffect:
    def __init__(self, effect_id, name, duration):
        self.effect_id = effect_id
        self.name = name
        self.duration = duration

    def apply(self, user, target, now):
        active_stun = ActiveStun(
            effect_id=self.effect_id,
            name=self.name,
            duration=self.duration,
            source=user,
            now=now
        )

        target.active_effects.append(active_stun)

        return active_stun
