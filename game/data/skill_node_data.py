from modules.skill_node_module import Node

STAT_NAMES = {
    "max_hp": "HP",
    "st": "STR",
    "df": "DEF",
    "mp": "MGP",
    "ev": "EVA",
    "cr": "CRT",
    "cd": "CRD",
    "hp_rr": "HRR",
    "hp_ra": "HRA"
}

COMMON_NODES = {
            "sharper_edge": Node(
                name="Sharper Edge",
                tooltip="Sharpen your weapon.",
                points=0,
                max_points=3,
                stats={"max_hp": 0, "st": 1, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon"]
            ),
            "full_body_callus": Node(
                name="Full Body Callus",
                tooltip="The skin on your body thickens.",
                points=0,
                max_points=3,
                stats={"max_hp": 0, "st": 0, "df": 1, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["armor"]
            ),
            "pain_tolerance": Node(
                name="Pain Tolerance",
                tooltip="Ignoring pain becomes easier.",
                points=0,
                max_points=3,
                stats={"max_hp": 3, "st": 0, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "cautious": Node(
                name="Cautious",
                tooltip="You always think before acting.",
                points=0,
                max_points=3,
                stats={"max_hp": 2, "st": 0, "df": 1, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon"]
            ),
            "reckless": Node(
                name="Reckless",
                tooltip="You love to charge in without a plan.",
                points=0,
                max_points=3,
                stats={"max_hp": 0, "st": 3, "df": -1, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon"]
            ),
            "confidence": Node(
                name="Confidence",
                tooltip="You believe in your ability to stand up to your opponents.",
                points=0,
                max_points=3,
                stats={"max_hp": 5, "st": 0, "df": 1, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "frail": Node(
                name="Frail",
                tooltip="Your body gets weaker.",
                points=0,
                max_points=3,
                stats={"max_hp": -5, "st": -1, "df": -1, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "turtle instincts": Node(
                name="Turtle Instincts",
                tooltip="You prioritize shielding yourself above all else.",
                points=0,
                max_points=3,
                stats={"max_hp": -15, "st": -3, "df": 5, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "block training": Node(
                name="Block Training",
                tooltip="You practice blocking blows from various angles.",
                points=0,
                max_points=3,
                stats={"max_hp": 0, "st": 0, "df": 1, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "weight lifting": Node(
                name="Weight Lifting",
                tooltip="Lifting weights helps you build muscle.",
                points=0,
                max_points=3,
                stats={"max_hp": 0, "st": 1, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "illness": Node(
                name="Illness",
                tooltip="The equipment's aura makes you nauseous.",
                points=0,
                max_points=3,
                stats={"max_hp": -10, "st": 0, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "handicap": Node(
                name="Handicap",
                tooltip="You're very confident in yourself.",
                points=0,
                max_points=3,
                stats={"max_hp": -10, "st": -3, "df": -3, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "goof off": Node(
                name="Goof Off",
                tooltip="You love wasting time.",
                points=0,
                max_points=3,
                stats={"max_hp": 0, "st": 0, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "first aid training": Node(
                name="First Aid Training",
                tooltip="You quickly tend to your wounds.",
                points=0,
                max_points=3,
                stats={"max_hp": 0, "st": 0, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0.3, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "quick reflexes": Node(
                name="Quick Reflexes",
                tooltip="Your reaction time gets better with practice.",
                points=0,
                max_points=3,
                stats={"max_hp": 0, "st": 0, "df": 0, "mp": 0, "ev": 1, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["armor"]
            ),
            "meditation": Node(
                name="Meditation",
                tooltip="Clear your mind when relaxing.",
                points=0,
                max_points=3,
                stats={"max_hp": 0, "st": 0, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 1},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "study": Node(
                name="Study",
                tooltip="Knowledge is power.",
                points=0,
                max_points=3,
                stats={"max_hp": 0, "st": 0, "df": 0, "mp": 1, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "called shot": Node(
                name="Called Shot",
                tooltip="You aim for their weak point.",
                points=0,
                max_points=3,
                stats={"max_hp": 0, "st": 0, "df": 0, "mp": 0, "ev": 0, "cr": 1, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "parry": Node(
                name="Parry",
                tooltip="You retaliate after dodging, doing +20 damage on the next auto attack.",
                points=0,
                max_points=1,
                stats={"max_hp": 0, "st": 0, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon"]
            ),
            "exterminator": Node(
                name="Exterminator",
                tooltip="Damage against insects increases by 5%.",
                points=0,
                max_points=3,
                stats={"max_hp": 0, "st": 0, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon"],
                damage_modifiers={"insect": 0.05}
            ),
            "nsuns": Node(
                name="nSuns",
                tooltip="High-volume progression lifting.",
                points=0,
                max_points=1,
                stats={"max_hp": 5, "st": 3, "df": 1, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "trained nerve endings": Node(
                name="Trained Nerve Endings",
                tooltip="You train your nerve endings to anticipate damage.",
                points=0,
                max_points=1,
                stats={"max_hp": 0, "st": 0, "df": 4, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "cardio": Node(
                name="Cardio",
                tooltip="You run 1 mile per rank every morning.",
                points=0,
                max_points=3,
                stats={"max_hp": 3, "st": 0, "df": 0, "mp": 0, "ev": 1, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["armor"]
            ),
            "accidental damage": Node(
                name="Accidental Damage",
                tooltip="You don't know your own strength.",
                points=0,
                max_points=3,
                stats={"max_hp": 0, "st": 0, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 3, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "immune system boost": Node(
                name="Immune System Boost",
                tooltip="Your body fights against the abnormal more efficiently.",
                points=0,
                max_points=3,
                stats={"max_hp": 8, "st": 0, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "bash": Node(
                name="Bash",
                tooltip="Bash the target with the hilt of your weapon for base 10 damage.",
                points=0,
                max_points=1,
                stats={},
                requires=[],
                unlocks=["bash"],
                skill_tags=["weapon"]
            ),
            "gash": Node(
                name="Gash",
                tooltip="Give the target a deep cut. Dealing 10 damage over 5 seconds.",
                points=0,
                max_points=1,
                stats={},
                requires=[],
                unlocks=["gash"],
                skill_tags=["weapon"]
            ),
            "quick hit": Node(
                name="Quick Hit",
                tooltip="Hit the target quickly for 5 damage. Fast cooldown.",
                points=0,
                max_points=1,
                stats={},
                requires=[],
                unlocks=["quick hit"],
                skill_tags=["weapon"]
            ),
            "head_rattle": Node(
                name="Head Rattle",
                tooltip="Hit the target on the head for 7 damage and stunning them for 2 seconds.",
                points=0,
                max_points=1,
                stats={},
                requires=[],
                unlocks=["head rattle"],
                skill_tags=["weapon"]
            )
        }

BLUE_NODES = {
            "fluid swings": Node(
                name="Fluid Swings",
                tooltip="Your swings are practiced and professional.",
                points=0,
                max_points=3,
                stats={"st": 3},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            )
}

YELLOW_NODES = {
            "evasive maneuvers": Node(
                name="Evasive Maneuvers",
                tooltip="Your agility improves.",
                points=0,
                max_points=3,
                stats={"ev": 1},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            )
}

PURPLE_NODES = {
            "captain's vigor": Node(
                name="Captain's Vigor",
                tooltip="Your vigor matches that of a captain in an army.",
                points=0,
                max_points=3,
                stats={"max_hp": 150, "st": 8, "df": 4},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            )
}

CAPSTONE_NODES = {
    "white": {
            "constitution boost": Node(
                name="Constitution Boost",
                tooltip="Your physical health inspires others.",
                points=0,
                max_points=1,
                stats={"max_hp": 30, "st": 0, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "blessing of health": Node(
                name="Blessing of Health",
                tooltip="You're blessed with good health. Every invested skill point on this piece of equipment "
                        "gains +2 HP in addition to its other bonuses.",
                points=0,
                max_points=1,
                stats={"max_hp": 0, "st": 0, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            # "apprentice": Node(
            #     name="Apprentice",
            #     tooltip="Equipment in your other slots gain +1 xp.",
            #     points=0,
            #     max_points=1,
            #     stats={"max_hp": 0, "st": 0, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
            #     requires=[],
            #     unlocks=[],
            #     skill_tags=["weapon", "armor"]
            # ),
            # "raw numbers": Node(
            #     name="Raw Numbers",
            #     tooltip="Increases your minimum damage by 3 and maximum damage by 5.",
            #     points=0,
            #     max_points=1,
            #     stats={"max_hp": 0, "st": 0, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
            #     requires=[],
            #     unlocks=[],
            #     skill_tags=["weapon"]
            # )
    },
    "green": {
            "level up": Node(
                name="Level Up",
                tooltip="You level up in a more traditional way.",
                points=0,
                max_points=1,
                stats={"max_hp": 10, "st": 5, "df": 5, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "procrastination devastation": Node(
                name="Procrastination Devastation",
                tooltip="Waiting until the last second will always bring efficiency. "
                        "Damage increases by 1% for every unspent skill point on this piece of equipment.",
                points=0,
                max_points=1,
                stats={"max_hp": 0, "st": 0, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "surge of strength": Node(
                name="Surge of Strength",
                tooltip="Your equipment suddenly feels much lighter.",
                points=0,
                max_points=1,
                stats={"max_hp": 0, "st": 15, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
    },
    "blue": {
            "troll dna": Node(
                name="Troll DNA",
                tooltip="Your regeneration is not natural.",
                points=0,
                max_points=1,
                stats={"hp_rr": 2.0, "hp_ra": 15},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
    },
    "yellow": {
            "curse of dwarfism": Node(
                name="Curse of Dwarfism",
                tooltip="You shrink to a smaller size affecting HP and EVA.",
                points=0,
                max_points=1,
                stats={"max_hp": -100, "ev": 20},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
    },
    "purple": {
            "effortless destruction": Node(
                name="Effortless Destruction",
                tooltip="Your blows can be devastating without you breaking a sweat.",
                points=0,
                max_points=1,
                stats={"cr": 30, "cd": 25},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
    }
}

NODE_POOLS = {"white": COMMON_NODES, "green": COMMON_NODES, "blue": BLUE_NODES, "yellow": YELLOW_NODES,
              "purple": PURPLE_NODES}



