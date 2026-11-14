class Pickup:

    def __init__(self, icon, hp, st, df):
        self.name = "Holy Shard",
        self.icon = icon
        self.hp = hp,
        self.st = st,
        self.df = df


class StrGem(Pickup):

    def __init__(self, icon="*", hp=0, st=1, df=0):

        super().__init__(icon, hp, st, df)


class DefGem(Pickup):

    def __init__(self, icon="*", hp=0, st=0, df=1):

        super().__init__(icon, hp, st, df)


class HPGem(Pickup):

    def __init__(self, icon="*", hp=5, st=0, df=0):

        super().__init__(icon, hp, st, df)


class UltimateGem(Pickup):

    def __init__(self, icon="*", hp=25, st=5, df=5):

        super().__init__(icon, hp, st, df)

