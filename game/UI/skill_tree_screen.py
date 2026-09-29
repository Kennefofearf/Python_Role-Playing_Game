import curses
import textwrap
from data.skill_node_data import CAPSTONE_NODES, STAT_NAMES, NODE_POOLS
from UI.colors import get_rarity_color, get_color_from_rarity, GREEN
import json

ASSIGN_HOTKEY = {ord("1"): "1", ord("2"): "2", ord("3"): "3", ord("4"): "4"}


def dbg(data):
    with open("debug.txt", "a") as f:
        f.write(json.dumps(data, indent=4))
        f.write("\n\n")


def get_node_tier_rarity(slot_index):
    if slot_index <= 8:
        return "white"
    elif slot_index <= 17:
        return "green"
    elif slot_index <= 26:
        return "blue"
    elif slot_index <= 35:
        return "yellow"
    else:
        return "purple"


def draw_node(window, y, x, label, node, is_selected, border_color):
    height, width = window.getmaxyx()

    node_height = 5
    node_width = 7

    if y < 1 or y + node_height >= height:
        return

    if x < 1 or x + node_width >= width:
        return

    border_attr = curses.color_pair(border_color)

    # draws the nodes
    window.addstr(y, x, "_____", border_attr)
    window.addstr(y + 1, x, "|     |", border_attr)
    window.addstr(y + 2, x, f"|{label:^5}|", border_attr)
    window.addstr(y + 3, x, "|_____|", border_attr)

    if is_selected:

        label_attr = curses.A_REVERSE

    if node.get("available", False):

        label_attr = curses.color_pair(2)

    else:

        label_attr = curses.A_NORMAL

    rank = f"{node['points']}/{node['max_points']}"
    window.addstr(y + 4, x + 1, rank, label_attr)


def draw_item_name(window, item, width):
    name = item["name"]
    item_color = get_rarity_color(item)
    xp = item["xp"]
    max_xp = item["max_xp"]

    title = f"{name}    {xp}/{max_xp}"
    window.addstr(1, max(1, (width - len(title)) / 2), title, item_color)


def draw_skill_tree_nodes(window, item, selected_slot, scroll):
    layout = item.skill_tree["layout"]

    for slot_index, position in enumerate(layout["slots"]):
        if position is None:
            continue

        y, x = position
        y -= scroll

        node = item.skill_tree["nodes"].get(slot_index)
        if not node:
            continue

        tier_rarity = get_node_tier_rarity(slot_index)
        border_color = get_color_from_rarity(tier_rarity)

        capstone_rarity = layout["capstones"].get(slot_index)

        if capstone_rarity:
            node_data = CAPSTONE_NODES[capstone_rarity][node["node_id"]]
        else:
            node_pool = NODE_POOLS[node["node_rarity"]]
            node_data = node_pool[node["node_id"]]

        label = node_data.name[:5]
        is_selected = slot_index == selected_slot

        draw_node(window, y, x, label, node, is_selected, border_color)


def unlock_adjacent_nodes(selected_item, selected_slot):
    skill_tree = selected_item.skill_tree
    nodes = skill_tree["nodes"]
    connections = skill_tree["layout"]["connections"]
    layout = skill_tree["layout"]

    for first_slot, second_slot in connections:
        if first_slot == selected_slot:
            if second_slot in nodes:
                nodes[second_slot]["available"] = True

        elif second_slot == selected_slot:
            if first_slot in nodes:
                nodes[first_slot]["available"] = True


def open_skill_tree(stdscr, selected_item, player):
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

    selected_slot = 0
    scroll_y = 0

    while True:
        stdscr_y, stdscr_x = stdscr.getmaxyx()
        height = int(stdscr_y * 0.7)
        tree_width = int(stdscr_x * 0.35)
        start_y = int(stdscr_y * 0.15)
        tree_x = int(stdscr_x * 0.55)

        skill_tree_window = curses.newwin(height, tree_width, start_y, tree_x)
        skill_tree_window.box()

        skill_tree_window_y, skill_tree_window_x = skill_tree_window.getbegyx()

        # draw_item_name(skill_tree_window, selected_item, width)
        draw_skill_tree_nodes(skill_tree_window, selected_item, selected_slot, scroll_y)
        skill_tree_window.refresh()

        key = stdscr.getch()

        if key == ord("q"):
            skill_tree_window.erase()
            skill_tree_window.refresh()
            break
        elif key == curses.KEY_MOUSE:
            _, mx, my, _, bstate, = curses.getmouse()

            wheel_up = getattr(curses, "BUTTON4_PRESSED", 65536)
            wheel_down = getattr(curses, "BUTTON5_PRESSED", 2097152)

            if wheel_up and (bstate & wheel_up):
                scroll_y = max(0, scroll_y - 2)

            elif wheel_down and (bstate & wheel_down):
                scroll_y += 2

            elif bstate & curses.BUTTON1_CLICKED:

                layout = selected_item.skill_tree["layout"]
                selected_slot = None

                mouse_y = my - skill_tree_window_y
                mouse_x = mx - skill_tree_window_x

                for slot_index, position in enumerate(layout["slots"]):
                    if position is None:
                        continue

                    y, x = position
                    y -= scroll_y

                    if y <= mouse_y <= y + 2 and x <= mouse_x <= x + 4:
                        selected_slot = slot_index
                        break

                if selected_slot is not None:
                    open_skill_tree_node_window(stdscr, selected_item, selected_slot, player)


def open_skill_tree_node_window(stdscr, selected_item, selected_slot, player):
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    node = selected_item.skill_tree["nodes"][selected_slot]

    if node.get("node_type") == "capstone":
        capstone_rarity = node["capstone_rarity"]
        node_data = CAPSTONE_NODES[capstone_rarity][node["node_id"]]
    else:
        node_pool = NODE_POOLS[node["node_rarity"]]
        node_data = node_pool[node["node_id"]]

    node_name = node_data.name
    node_tooltip = node_data.tooltip

    wrapped_tooltip = textwrap.wrap(node_tooltip, 34, break_long_words=True, break_on_hyphens=True)

    node_rank = node["points"]
    max_node_rank = node_data.max_points

    available_skill_points = selected_item.skill_points

    while True:

        stdscr_y, stdscr_x = stdscr.getmaxyx()
        height = int(stdscr_y * 0.7)
        tree_width = int(stdscr_x * 0.35)
        start_y = int(stdscr_y * 0.15)
        tree_x = int(stdscr_x * 0.55)

        node_description_window = curses.newwin(height, tree_width, start_y, tree_x)
        node_description_window.box()

        row = 3

        node_description_window.addstr(1, (int(tree_width / 2) - int(len(node_name) / 2)),
                                       f"{node_name}")
        for line in wrapped_tooltip:
            node_description_window.addstr(row, 2, f"{line}")
            row += 1

        for stat, value in node_data.stats.items():
            if value == 0:
                continue
            display_name = STAT_NAMES.get(stat, stat)

            row += 1
            node_description_window.addstr(row, 2, f"{display_name}: {value}")

        row += 3

        if selected_item.has_node("blessing of health") and node["points"] > 0:
            node_description_window.addstr(row, 2, f"Blessing of Health (HP: {2 * node['points']})",
                                           curses.color_pair(GREEN))
            row += 2

        node_description_window.addstr(row, 2, f"Rank: {node_rank}/{max_node_rank}")
        row += 1
        node_description_window.addstr(row, 2, f"Available Points: {available_skill_points}")

        node_description_window.refresh()

        key = stdscr.getch()

        if key in (27, ord("q")):
            break

        if key == ord("a"):
            if node_rank < max_node_rank and available_skill_points > 0 and node["available"]:
                node["points"] += 1
                selected_item.skill_points -= 1

                if 0 < node["points"] < 2:
                    player.get_boh_bonus()

                for ability_id in node_data.unlocks:
                    selected_item.unlock_ability(ability_id)

                    if selected_item == player.weapon:
                        player.auto_equip_ability(ability_id)

                node_rank = node["points"]
                available_skill_points = selected_item.skill_points

                unlock_adjacent_nodes(selected_item, selected_slot)

            elif node_rank >= max_node_rank:
                row += 1
                node_description_window.addstr(row, 2, f"Skill is at max rank!")

            elif available_skill_points <= 0:
                row += 1
                node_description_window.addstr(row, 2, f"No skill points available!")

            elif not node["available"]:
                row += 1
                node_description_window.addstr(row, 2, f"Node is not yet unlocked.")

        elif key in ASSIGN_HOTKEY:
            if node_rank > 0 and selected_item == player.weapon:
                slot = ASSIGN_HOTKEY[key]
                for ability_id in node_data.unlocks:
                    player.equip_ability(ability_id, slot)

            node_description_window.refresh()


