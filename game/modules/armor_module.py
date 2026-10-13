from modules.item_module import Item
from data.affix_data import ALL_AFFIXES
from systems.items.item_scaling import get_item_level_multiplier, get_base_ac_multiplier


class Armor(Item):

    def __init__(self):
        super().__init__()

        self.base_ac = 0
        self.slot = ""

    @property
    def ac(self):
        bonus = 0

        for affix_id in self.affixes:
            affix = ALL_AFFIXES[affix_id]
            multiplier = get_item_level_multiplier(self.item_lvl, affix.rarity)
            bonus += round(affix.ac * multiplier)

        base_multiplier = get_base_ac_multiplier(self.item_lvl)
        scaled_base_ac = round(self.base_ac * base_multiplier)

        return scaled_base_ac + bonus
