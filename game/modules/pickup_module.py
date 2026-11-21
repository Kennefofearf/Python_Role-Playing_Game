class Pickup:

    def __init__(self, name, icon, hp, st, df, hra, ev):
        self.name = name
        self.icon = icon
        self.hp = hp
        self.st = st
        self.df = df
        self.hra = hra
        self.ev = ev

    def gem_log_message(self, add_log_messages, combat_messages):
        add_log_messages(combat_messages, [(f"Picked up a ", 0), (f"{self.name}", 10),(f"!", 0),
                                           (f" Stats permanently increased!", 0)])

class StrGem(Pickup):

    def __init__(self, name="Strength Gem", icon="*", hp=0, st=1, df=0, hra=0, ev=0):

        super().__init__(name, icon, hp, st, df, hra, ev)


class DefGem(Pickup):

    def __init__(self, name="Defense Gem", icon="*", hp=0, st=0, df=1, hra=0, ev=0):

        super().__init__(name, icon, hp, st, df, hra, ev)




class HPGem(Pickup):

    def __init__(self, name="HP Gem", icon="*", hp=5, st=0, df=0, hra=0, ev=0):

        super().__init__(name, icon, hp, st, df, hra, ev)


class EvaGem(Pickup):

    def __init__(self, name="Evasion Gem", icon="*", hp=0, st=0, df=0, hra=0, ev=0.5):

        super().__init__(name, icon, hp, st, df, hra, ev)


class ReGem(Pickup):

    def __init__(self, name="Regen Gem", icon="*", hp=0, st=0, df=0, hra=1, ev=0):

        super().__init__(name, icon, hp, st, df, hra, ev)


class UltimateGem(Pickup):

    def __init__(self, name="Ultimate Gem", icon="*", hp=25, st=5, df=5, hra=0, ev=0):

        super().__init__(name, icon, hp, st, df, hra, ev)

