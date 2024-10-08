import time

def right(stdscr, name_profile, player_x, player_y, name_x, name_y, max_width):
    from controllers.game_control import game_control
    stdscr.addstr(player_y, player_x, " ")
    stdscr.addstr(name_y, name_x, " " * len(name_profile))
    time.sleep(0.02)
    player_x += 1
    name_x += 1
    stdscr.addstr(player_y, player_x, "🦖")
    stdscr.addstr(name_y, name_x, name_profile)
    stdscr.refresh()
    return game_control(stdscr, name_profile, player_x, player_y, name_x, name_y, max_width)