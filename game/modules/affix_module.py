import random


class Affix:

    def __init__(self, name, affix_type, affix_stats, ac, min_dmg, max_dmg, item_type, rarity):
        self.name = name
        self.affix_type = affix_type
        self.affix_stats = affix_stats
        self.ac = ac
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.item_type = item_type
        self.rarity = rarity