# def world_event_logic(player, py, px, stdscr, combat_messages, inner, scroll_offset, enemy_window, game_map, start_y,
#                       start_x, camera):
#     now = time.time()
#
#     win_y, win_x = enemy_window.getbegyx()
#     win_h, win_w = enemy_window.getmaxyx()
#
#     player.regenerate_hp(now)
#     update_active_effects(player, now, combat_messages)
#     ny, nx = player.future_position(py, px)
#     py, px = collision_check(game_map, py, px, ny, nx)
#
#     if not inside_map(game_map, ny, nx):
#         py, px = 0, 0
#         ny, nx = player.future_position(py, px)
#
#     player_hit = player_auto_attack_logic(player, add_log_messages, combat_messages)
#     enemy_hit = enemy_auto_attack_logic(enemies, player, add_log_messages, combat_messages)
#
#     if player_hit or enemy_hit:
#         draw_log(inner, combat_messages, scroll_offset)
#
#     if player.player_death:
#         add_log_messages(combat_messages, [(f"RIP...", 1)])
#         draw_log(inner, combat_messages, scroll_offset)
#         screen_y, screen_x = camera.world_to_screen(player.position[0], player.position[1], start_y, start_x)
#         stdscr.addstr(screen_y, screen_x, player.icon, curses.color_pair(RED_BG))
#         stdscr.refresh()
#         time.sleep(3)
#         return True
#
#     for e in enemies:
#
#         update_active_effects(e, now, combat_messages)
#
#         e.respawn_timer(player)
#         if not e.alive:
#             continue
#
#         is_stunned = any(effect.effect_id == "stun" for effect in e.active_effects)
#
#         if is_stunned:
#             ey = 0
#             ex = 0
#         else:
#             ey, ex = e.enemy_random_movement()
#             ey, ex = e.aggro(player)
#
#         ney, nex = e.future_position(ey, ex)
#         ey, ex = collision_check(game_map, ey, ex, ney, nex)
#
#         if not inside_map(game_map, ney, nex):
#             ey = 0
#             ex = 0
#
#         elif (ney, nex) == tuple(player.position):
#             ey = 0
#             ex = 0
#
#         elif (ny, nx) == tuple(e.position):
#             py = 0
#             px = 0
#
#         elif (ny, nx) == (ney, nex):
#             py = 0
#             px = 0
#
#         if not e.movement_range(ey, ex) and not e.is_aggroed:
#             # if not e.is_attacking and e.return_home():
#             #     ey -= e.position[0] - e.home_position[0]
#             #     ex -= e.position[1] - e.home_position[1]
#
#             ey, ex = 0, 0
#
#         e.move(ey, ex)
#
#     for gem in gems:
#         if player.position == gem.position:
#             player.base_st += gem.st
#             player.base_df += gem.df
#             player.base_max_hp += gem.hp
#             player.base_evasion += gem.ev
#             player.base_hp_ra += gem.hra
#
#             player.collected_gems.append(gem.id)
#             gem.gem_log_message(add_log_messages, combat_messages)
#             gems.remove(gem)
#
#
#     player.move(py, px)
#
#     return False
#
#
# def movement_area(win, y, x):
#     h, w = win.getmaxyx()
#     return 1 <= y <= h - 2 and 1 <= x <= w - 2
#
#
# def inside_map(game_map, y, x):
#     return (
#         0 <= y < len(game_map) and 0 <= x < len(game_map[y])
#     )