import random
from modules.item_module import Item
from data.skill_node_data import COMMON_NODES, CAPSTONE_NODES, NODE_POOLS


class Player:
    def __init__(self, name):
        self.name = name
        self.icon = "@"
        self._hp = 50
        self.base_max_hp = 50
        self.base_st = 3
        self.base_df = 1
        self.base_ac = 0
        self.base_mp = 0
        self.base_evasion = 3
        self.base_crit_rate = 3
        self.base_crit_dmg = 50
        self.base_hp_rr = 10.0
        self.base_hp_ra = 5
        self.inventory = []
        self.position = [0, 0]

        # combat

        self.attack_cooldown = 1.0
        self.weapon_dmg = [0, 0]
        self.damaged = False
        self.active_effects = []
        self.cooldowns = {}

        # combat passives

        self.parry_ready = False

        # progression

        self.req_xp = 8
        self.total_req_xp = 8
        self.xp_bar_text = ''
        self.lvl = 1

        # equipment

        self.weapon = None
        self.feet = None
        self.chest = None
        self.head = None
        self.target = None

        # build

        self.skill_tree = {}
        self.ability_slots = {"1": None, "2": None, "3": None, "4": None}
        self.magic_slots = {}
        self.last_attack_time = 0
        self.last_regen_time = 0

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, min(value, self.base_max_hp))

    @property
    def max_hp(self):
        bonus = 0

        equipment = [self.weapon, self.head, self.chest, self.feet]

        for item in equipment:
            if item is None:
                continue
            bonus += Item.total_bonus(item, "max_hp")

        bonus += self.get_boh_bonus()

        return self.base_max_hp + bonus

    # @max_hp.setter
    # def max_hp(self, value):
    #     self._max_hp = max(1, value)
    #
    #     if self._hp > self.max_hp:
    #         self._hp = self.max_hp

    @property
    def st(self):
        bonus = 0

        equipment = [self.weapon, self.head, self.chest, self.feet]

        for item in equipment:
            if item is None:
                continue
            bonus += Item.total_bonus(item, "st")

        return self.base_st + bonus

    # @st.setter
    # def st(self, value):
    #     self._st = max(0, value)

    @property
    def df(self):
        bonus = 0

        equipment = [self.weapon, self.head, self.chest, self.feet]

        for item in equipment:
            if item is None:
                continue

            bonus += Item.total_bonus(item, "df")

        return self.base_df + bonus

    @property
    def ac(self):
        total = 0

        armor = [self.head, self.chest, self.feet]

        for item in armor:
            if item is None:
                continue

            total += item.ac

        return total

    @property
    def mp(self):
        bonus = 0

        equipment = [self.weapon, self.head, self.chest, self.feet]

        for item in equipment:
            if item is None:
                continue
            bonus += Item.total_bonus(item, "mp")

        return self.base_mp + bonus

    @property
    def evasion(self):
        bonus = 0

        equipment = [self.weapon, self.head, self.chest, self.feet]

        for item in equipment:
            if item is None:
                continue
            bonus += Item.total_bonus(item, "ev")

        return min(80, max(0, self.base_evasion + bonus))

    @property
    def crit_rate(self):
        bonus = 0

        equipment = [self.weapon, self.head, self.chest, self.feet]

        for item in equipment:
            if item is None:
                continue
            bonus += Item.total_bonus(item, "cr")

        return min(100, max(0, self.base_crit_rate + bonus))

    @property
    def crit_dmg(self):
        bonus = 0

        equipment = [self.weapon, self.head, self.chest, self.feet]

        for item in equipment:
            if item is None:
                continue
            bonus += Item.total_bonus(item, "cd")

        return max(0, self.base_crit_dmg + bonus)

    @property
    def hp_rr(self):
        bonus = 0

        equipment = [self.weapon, self.head, self.chest, self.feet]

        for item in equipment:
            if item is None:
                continue
            bonus += Item.total_bonus(item, "hp_rr")

        return max(1.0, self.base_hp_rr - bonus)

    @property
    def hp_ra(self):
        bonus = 0

        equipment = [self.weapon, self.head, self.chest, self.feet]

        for item in equipment:
            if item is None:
                continue
            bonus += Item.total_bonus(item, "hp_ra")

        return self.base_hp_ra + bonus

    @property
    def player_death(self):
        return self._hp <= 0

    def get_pro_dev_bonus(self):
        bonus_dmg = 0

        for item in [self.weapon, self.head, self.chest, self.feet]:
            if not item:
                continue

            if item.has_node("procrastination devastation"):
                percent_bonus = (0.01 * item.skill_points)
                bonus_dmg += percent_bonus

        return bonus_dmg

    def get_boh_bonus(self):
        bonus = 0

        for item in [self.weapon, self.head, self.chest, self.feet]:
            if not item:
                continue

            if item.has_node("blessing of health"):
                for node in item.skill_tree["nodes"].values():

                    bonus += 2 * node["points"]

        return bonus

    def get_species_damage_bonus(self, species):
        bonus_dmg = 0

        for item in [self.weapon, self.head, self.chest, self.feet]:
            if not item:
                continue

            for node in item.skill_tree["nodes"].values():
                if node["points"] > 0:

                    if node["node_type"] == "capstone":
                        node_pool = CAPSTONE_NODES[node["capstone_rarity"]]
                        node_data = node_pool[node["node_id"]]
                    else:
                        node_pool = NODE_POOLS[node["node_rarity"]]
                        node_data = node_pool[node["node_id"]]

                    if species in node_data.damage_modifiers:
                        bonus_dmg += node_data.damage_modifiers[species] * node["points"]

        return bonus_dmg

    def has_equipped_ability(self, ability_id):

        equipment = [self.weapon, self.head, self.chest, self.feet]

        for item in equipment:
            if item and ability_id in item.unlocked_abilities:
                return True

    def equip_ability(self, ability_id, slot):
        if not self.has_equipped_ability(ability_id):
            return False

        self.ability_slots[slot] = ability_id
        return True

    def auto_equip_ability(self, ability_id):
        if not self.has_equipped_ability(ability_id):
            return False

        for slot, equipped_ability in self.ability_slots.items():
            if equipped_ability is None:
                self.ability_slots[slot] = ability_id
                return True

        return False

    def regenerate_hp(self, now):
        if self.hp < self.max_hp and now - self.last_regen_time >= self.hp_rr:
            self.hp += self.hp_ra
            self.last_regen_time = now

    def move(self, py, px):
        self.position[0] += py
        self.position[1] -= px

        if py != 0 or px != 0:
            if self.feet:
                Item.gain_item_xp(self.feet, 1)

            if self.head:
                Item.gain_item_xp(self.head, 1)

    def future_position(self, py, px):
        return self.position[0] + py, self.position[1] - px

    def take_dmg(self, dmg):
        if dmg <= 0:
            dmg = 0
        self._hp -= dmg
        self.damaged = True
        if self._hp <= 0:
            self._hp = 0

    # Updates the XP bar

    def update_xp_bar(self):
        progress = self.total_req_xp - self.req_xp
        bar_count = int((progress / self.total_req_xp) * 10)

        self.xp_bar_text = '=' * bar_count

    # Calculates XP gain and uses it to update the XP bar

    def xp_gain(self, xp):
        self.req_xp -= xp

        while self.req_xp <= 0:
            xp_overflow = -self.req_xp
            self.lvl += 1
            hp_gain = random.choice([5, 7, 7, 7, 10, 20])
            self.base_max_hp += hp_gain
            self._hp += hp_gain
            self.total_req_xp += 5 + self.lvl * 5
            self.req_xp = self.total_req_xp - xp_overflow

        self.update_xp_bar()

    def input_action(self, key):
        py, px = 0, 0
        if key == ord("a"):
            px = 1
        elif key == ord("d"):
            px = -1
        elif key == ord("w"):
            py = -1
        elif key == ord("s"):
            py = 1
        elif key == "":
            py, px = 0, 0
        return py, px

    def player_spawn(self, stdscr, prev_positions, camera, start_y, start_x):
        screen_y, screen_x = camera.world_to_screen(self.position[0], self.position[1], start_y, start_x)

        if (start_y <= screen_y < start_y + camera.height and start_x <= screen_x < start_x + camera.width):
            stdscr.addch(screen_y, screen_x, self.icon)
            prev_positions.append((screen_y, screen_x))
