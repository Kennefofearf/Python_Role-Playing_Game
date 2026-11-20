class Pickup:

    def __init__(self, icon, hp, st, df, hra, ev):
        self.name = None
        self.icon = icon
        self.hp = hp
        self.st = st
        self.df = df
        self.hra = hra
        self.ev = ev


class StrGem(Pickup):

    def __init__(self, icon="*", hp=0, st=1, df=0, hra=0, ev=0):

        super().__init__(icon, hp, st, df, hra, ev)


class DefGem(Pickup):

    def __init__(self, icon="*", hp=0, st=0, df=1, hra=0, ev=0):

        super().__init__(icon, hp, st, df, hra, ev)


class HPGem(Pickup):

    def __init__(self, icon="*", hp=5, st=0, df=0, hra=0, ev=0):

        super().__init__(icon, hp, st, df, hra, ev)


class EvaGem(Pickup):

    def __init__(self, icon="*", hp=0, st=0, df=0, hra=0, ev=0.5):

        super().__init__(icon, hp, st, df, hra, ev)


class ReGem(Pickup):

    def __init__(self, icon="*", hp=0, st=0, df=0, hra=1, ev=0):

        super().__init__(icon, hp, st, df, hra, ev)


class UltimateGem(Pickup):

    def __init__(self, icon="*", hp=25, st=5, df=5, hra=0, ev=0):

        super().__init__(icon, hp, st, df, hra, ev)

