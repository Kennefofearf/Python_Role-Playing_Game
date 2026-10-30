import curses
import time
import random
import pdb


class Monster:

    def __init__(self, name, icon, lvl, max_hp, hp, st, df, ac, mp, evasion, crit_rate,
                 crit_dmg, hp_rr, hp_ra, species, xp, respawn_delay, attack_cooldown, drop_chance):
        self.name = name
        self.icon = icon
        self.lvl = lvl
        self.max_hp = max_hp
        self.hp = hp
        self.st = st
        self.df = df
        self.ac = ac
        self.mp = mp
        self.evasion = evasion
        self.crit_rate = crit_rate
        self.crit_dmg = crit_dmg
        self.hp_rr = hp_rr
        self.hp_ra = hp_ra
        self.species = species
        self.position = [random.randint(2, 19), random.randint(2, 99)]
        self.home_position = self.position.copy()
        self.move_radius = 3
        self.is_aggroed = False
        self.alive = True
        self.xp = xp
        self.respawn_delay = respawn_delay
        self.attack_cooldown = attack_cooldown
        self.last_attack_time = 0
        self.is_attacking = False
        self.damaged = False
        self.active_effects = []
        self.ey = 0
        self.ex = 0
        self.random_movement = random.randint(1, 10)
        self.random_direction = random.randint(-1, 1)
        self.drop_chance = drop_chance

        self.idle = 0.0

    def enemy_random_movement(self):
        ey, ex = 0, 0
        if not self.is_attacking:

            now = time.monotonic()
            if now < self.idle:
                return 0, 0

            ey = random.choice([-1, 0, 1])
            ex = random.choice([-1, 0, 1])

            if random.randint(1, 3) == 1:
                self.idle = now + random.uniform(2, 4)

            return ey, ex
        return ey, ex

    def move(self, ey, ex):
        if not self.is_attacking:
            if self.alive:
                self.position[0] += ey
                self.position[1] -= ex
        return

    def movement_range(self, ey, ex):
        next_y, next_x = self.future_position(ey, ex)
        home_y, home_x = self.home_position

        return (
            abs(next_y - home_y) <= self.move_radius
            and abs(next_x - home_x) <= self.move_radius
        )

    def return_home(self):
        home_y, home_x = self.home_position

        return (self.position[0] > home_y + 3 or self.position[0] < home_y - 3
                and self.position[1] > home_x + 3 or self.position[1] < home_x - 3)

    def aggro(self, player):
        ey, ex = 0, 0

        dy = player.position[0] - self.position[0]
        dx = player.position[1] - self.position[1]

        in_range = abs(dy) <= 5 and abs(dx) <= 5

        if not self.is_attacking and self.alive:
            if in_range:
                self.is_aggroed = True
                if dy != 0:
                    ey = (dy > 0) - (dy < 0)
                elif dx != 0:
                    ex = (dx < 0) - (dx > 0)
            else:
                ey, ex = self.enemy_random_movement()

        return ey, ex


    def future_position(self, ey, ex):
        return self.position[0] + ey, self.position[1] - ex

    def take_dmg(self, dmg):
        self.hp -= dmg
        self.damaged = True
        if self.hp <= 0:
            self.hp = 0
            self.respawn_delay = time.monotonic() + 3
            self.alive = False

    def respawn_timer(self, player):
        if not self.alive and self.respawn_delay is not None and time.monotonic() >= self.respawn_delay:
            self.alive = True
            self.hp = self.max_hp
            self.respawn_delay = None
            self.position = [random.randint(2, 19), random.randint(2, 99)]
            while self.position == player.position:
                self.position = [random.randint(2, 19), random.randint(2, 99)]


class GiantAnt(Monster):
    def __init__(self, name="Giant Ant", icon="a", lvl=2, max_hp=60, hp=60, st=5, df=1, ac=0, mp=0, evasion=1,
                 crit_rate=0, crit_dmg=0, hp_rr=5, hp_ra=1, species="insect",
                 xp=2):
        super().__init__(name, icon, lvl, max_hp, hp, st, df, ac, mp, evasion, crit_rate, crit_dmg, hp_rr, hp_ra,
                         species, xp,
                         respawn_delay=None, attack_cooldown=2.0,
                         drop_chance=0.2)


class AntWarrior(Monster):
    def __init__(self, name="Ant Warrior", icon="a", lvl=12, max_hp=700, hp=700, st=16, df=6, ac=0, mp=0, evasion=1,
                 crit_rate=0, crit_dmg=0, hp_rr=5, hp_ra=3, species="insect",
                 xp=21):
        super().__init__(name, icon, lvl, max_hp, hp, st, df, ac, mp, evasion, crit_rate, crit_dmg, hp_rr, hp_ra,
                         species, xp,
                         respawn_delay=None, attack_cooldown=2.0,
                         drop_chance=0.2)


class AntWorker(Monster):
    def __init__(self, name="Ant Worker", icon="a", lvl=9, max_hp=400, hp=400, st=10, df=2, ac=0, mp=0, evasion=1,
                 crit_rate=0, crit_dmg=0, hp_rr=5, hp_ra=3, species="insect",
                 xp=11):
        super().__init__(name, icon, lvl, max_hp, hp, st, df, ac, mp, evasion, crit_rate, crit_dmg, hp_rr, hp_ra,
                         species, xp,
                         respawn_delay=None, attack_cooldown=2.0,
                         drop_chance=0.2)


class AntElite(Monster):
    def __init__(self, name="--[Elite Ant]--", icon="A", lvl=12, max_hp=1000, hp=1000, st=25, df=10, ac=0, mp=0,
                 evasion=1, crit_rate=0, crit_dmg=0, hp_rr=15, hp_ra=10, species="insect",
                 xp=50):
        super().__init__(name, icon, lvl, max_hp, hp, st, df, ac, mp, evasion, crit_rate, crit_dmg, hp_rr, hp_ra,
                         species, xp,
                         respawn_delay=None, attack_cooldown=1.5,
                         drop_chance=0.2)


class RoyalScoutAnt(Monster):
    def __init__(self, name="--[Royal Scout Ant]--", icon="A", lvl=18, max_hp=2500, hp=2500, st=32, df=12, ac=0, mp=0,
                 evasion=5, crit_rate=5, crit_dmg=50, hp_rr=10, hp_ra=30, species="insect",
                 xp=62):
        super().__init__(name, icon, lvl, max_hp, hp, st, df, ac, mp, evasion, crit_rate, crit_dmg, hp_rr, hp_ra,
                         species, xp,
                         respawn_delay=None, attack_cooldown=2.0,
                         drop_chance=0.2)


class RoyalWarriorAnt(Monster):
    def __init__(self, name="--[Royal Warrior Ant]--", icon="A", lvl=20, max_hp=4000, hp=4000, st=40, df=16, ac=0, mp=0,
                 evasion=5, crit_rate=5, crit_dmg=50, hp_rr=10, hp_ra=50, species="insect",
                 xp=75):
        super().__init__(name, icon, lvl, max_hp, hp, st, df, ac, mp, evasion, crit_rate, crit_dmg, hp_rr, hp_ra,
                         species, xp,
                         respawn_delay=None, attack_cooldown=2.0,
                         drop_chance=0.2)


class RoyalGuardAnt(Monster):
    def __init__(self, name="--[Royal Guard Ant]--", icon="A", lvl=23, max_hp=5500, hp=5500, st=65, df=25, ac=0, mp=0,
                 evasion=5, crit_rate=5, crit_dmg=50, hp_rr=10, hp_ra=100, species="insect",
                 xp=150):
        super().__init__(name, icon, lvl, max_hp, hp, st, df, ac, mp, evasion, crit_rate, crit_dmg, hp_rr, hp_ra,
                         species, xp,
                         respawn_delay=None, attack_cooldown=0.5,
                         drop_chance=0.2)


class AntQueen(Monster):
    def __init__(self, name="~~{Ant Queen}~~", icon="A", lvl=25, max_hp=9000, hp=9000, st=87, df=30, ac=0, mp=0, evasion=10,
                 crit_rate=5, crit_dmg=50, hp_rr=10, hp_ra=200, species="insect",
                 xp=500):
        super().__init__(name, icon, lvl, max_hp, hp, st, df, ac, mp, evasion, crit_rate, crit_dmg, hp_rr, hp_ra,
                         species, xp,
                         respawn_delay=None, attack_cooldown=2.5,
                         drop_chance=1.0)


class GiantSpider(Monster):
    def __init__(self, name="Giant Spider", icon="s", lvl=7, max_hp=750, hp=750, st=20, df=0, ac=0, mp=0, evasion=1,
                 crit_rate=0, crit_dmg=0, hp_rr=2, hp_ra=3, species="insect",
                 xp=16):
        super().__init__(name, icon, lvl, max_hp, hp, st, df, ac, mp, evasion, crit_rate, crit_dmg, hp_rr, hp_ra,
                         species, xp,
                         respawn_delay=None, attack_cooldown=0.5,
                         drop_chance=0.2)


class Crab(Monster):
    def __init__(self, name="Crab", icon="c", lvl=5, max_hp=500, hp=500, st=25, df=9, ac=0, mp=0, evasion=0,
                 crit_rate=0, crit_dmg=0, hp_rr=5, hp_ra=1, species="beast", xp=16):
        super().__init__(name, icon, lvl, max_hp, hp, st, df, ac, mp, evasion, crit_rate, crit_dmg, hp_rr, hp_ra,
                         species, xp,
                         respawn_delay=None, attack_cooldown=2.5,
                         drop_chance=0.2)


class KoboldScout(Monster):
    def __init__(self, name="Kobold", icon="k", lvl=3, max_hp=200, hp=200, st=15, df=5, ac=0, mp=0, evasion=1,
                 crit_rate=0, crit_dmg=0, hp_rr=5, hp_ra=1, species="humanoid",
                 xp=8):
        super().__init__(name, icon, lvl, max_hp, hp, st, df, ac, mp, evasion, crit_rate, crit_dmg, hp_rr, hp_ra,
                         species, xp,
                         respawn_delay=None, attack_cooldown=1.0,
                         drop_chance=0.2)


class KoboldWorker(Monster):
    def __init__(self, name="Kobold Worker", icon="k", lvl=4, max_hp=280, hp=280, st=18, df=6, ac=0, mp=0, evasion=1,
                 crit_rate=0, crit_dmg=0, hp_rr=5, hp_ra=1, species="humanoid",
                 xp=12):
        super().__init__(name, icon, lvl, max_hp, hp, st, df, ac, mp, evasion, crit_rate, crit_dmg, hp_rr, hp_ra,
                         species, xp,
                         respawn_delay=None, attack_cooldown=2.0,
                         drop_chance=0.2)


class KoboldHunter(Monster):
    def __init__(self, name="Kobold Hunter", icon="k", lvl=7, max_hp=550, hp=550, st=21, df=7, ac=0, mp=0, evasion=1,
                 crit_rate=5, crit_dmg=50, hp_rr=5, hp_ra=1, species="humanoid",
                 xp=18):
        super().__init__(name, icon, lvl, max_hp, hp, st, df, ac, mp, evasion, crit_rate, crit_dmg, hp_rr, hp_ra,
                         species, xp,
                         respawn_delay=None, attack_cooldown=1.0,
                         drop_chance=0.2)


class KoboldWarrior(Monster):
    def __init__(self, name="Kobold Warrior", icon="k", lvl=15, max_hp=1200, hp=1200, st=28, df=11, ac=0, mp=0, evasion=4,
                 crit_rate=5, crit_dmg=50, hp_rr=5, hp_ra=5, species="humanoid",
                 xp=26):
        super().__init__(name, icon, lvl, max_hp, hp, st, df, ac, mp, evasion, crit_rate, crit_dmg, hp_rr, hp_ra,
                         species, xp,
                         respawn_delay=None, attack_cooldown=1.0,
                         drop_chance=0.2)


class KoboldElite(Monster):
    def __init__(self, name="--[Kobold Elite]--", icon="K", lvl=22, max_hp=3000, hp=3000, st=38, df=16, ac=0, mp=0, evasion=8,
                 crit_rate=5, crit_dmg=50, hp_rr=5, hp_ra=60, species="humanoid",
                 xp=80):
        super().__init__(name, icon, lvl, max_hp, hp, st, df, ac, mp, evasion, crit_rate, crit_dmg, hp_rr, hp_ra,
                         species, xp,
                         respawn_delay=None, attack_cooldown=1.5,
                         drop_chance=0.2)


class KoboldChief(Monster):
    def __init__(self, name="~~{Kobold Chief}~~", icon="K", lvl=27, max_hp=7500, hp=7500, st=50, df=22, ac=0, mp=0, evasion=7,
                 crit_rate=5, crit_dmg=50, hp_rr=5, hp_ra=150, species="humanoid",
                 xp=600):
        super().__init__(name, icon, lvl, max_hp, hp, st, df, ac, mp, evasion, crit_rate, crit_dmg, hp_rr, hp_ra,
                         species, xp,
                         respawn_delay=None, attack_cooldown=1.5,
                         drop_chance=1.0)


class Bear(Monster):
    def __init__(self, name="Bear", icon="b", lvl=4, max_hp=350, hp=350, st=20, df=8, ac=0, mp=0, evasion=1,
                 crit_rate=0, crit_dmg=0, hp_rr=5, hp_ra=1, species="beast",
                 xp=12):
        super().__init__(name, icon, lvl, max_hp, hp, st, df, ac, mp, evasion, crit_rate, crit_dmg, hp_rr, hp_ra,
                         species, xp,
                         respawn_delay=None, attack_cooldown=2.0,
                         drop_chance=0.2)


class Deer(Monster):
    def __init__(self, name="Deer", icon="d", lvl=4, max_hp=300, hp=300, st=15, df=1, ac=0, mp=0, evasion=10,
                 crit_rate=0, crit_dmg=0, hp_rr=5, hp_ra=1, species="beast",
                 xp=9):
        super().__init__(name, icon, lvl, max_hp, hp, st, df, ac, mp, evasion, crit_rate, crit_dmg, hp_rr, hp_ra,
                         species, xp,
                         respawn_delay=None, attack_cooldown=1.0,
                         drop_chance=0.2)


class Snake(Monster):
    def __init__(self, name="Snake", icon="s", lvl=6, max_hp=600, hp=600, st=20, df=2, ac=0, mp=0, evasion=10,
                 crit_rate=0, crit_dmg=0, hp_rr=5, hp_ra=1, species="beast",
                 xp=14):
        super().__init__(name, icon, lvl, max_hp, hp, st, df, ac, mp, evasion, crit_rate, crit_dmg, hp_rr, hp_ra,
                         species, xp,
                         respawn_delay=None, attack_cooldown=2.0,
                         drop_chance=0.2)


class Boar(Monster):
    def __init__(self, name="Boar", icon="b", lvl=3, max_hp=250, hp=250, st=18, df=1, ac=0, mp=0, evasion=5,
                 crit_rate=0, crit_dmg=0, hp_rr=30, hp_ra=5, species="beast",
                 xp=8):
        super().__init__(name, icon, lvl, max_hp, hp, st, df, ac, mp, evasion, crit_rate, crit_dmg, hp_rr, hp_ra,
                         species, xp,
                         respawn_delay=None, attack_cooldown=1.8,
                         drop_chance=0.2)

# Rakarz is Polish for: the one who flays


class Rakarz(Monster):
    def __init__(self, name="~~{Rakarz, the Lion of the Fields}~~", icon="R", lvl=30, max_hp=9000, hp=9000, st=62, df=26, ac=0, mp=0, evasion=15,
                 crit_rate=5, crit_dmg=50, hp_rr=5, hp_ra=50, species="beast",
                 xp=700):
        super().__init__(name, icon, lvl, max_hp, hp, st, df, ac, mp, evasion, crit_rate, crit_dmg, hp_rr, hp_ra,
                         species, xp,
                         respawn_delay=None, attack_cooldown=1.0,
                         drop_chance=1.0)
