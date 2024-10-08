import time

def jump(stdscr, name_profile, player_x, player_y, name_x, name_y, max_width):
    from controllers.game_control import game_control
    stdscr.addstr(name_y, name_x, " " * len(name_profile))
    stdscr.addstr(player_y, player_x, " ")
    time.sleep(0.035)
    stdscr.addstr(name_y - 2, name_x, name_profile)
    stdscr.addstr(player_y - 2, player_x, "🦖")
    stdscr.refresh()
    time.sleep(0.035)
    stdscr.addstr(name_y - 2, name_x, " " * len(name_profile))
    stdscr.addstr(player_y - 2, player_x, " ")
    time.sleep(0.035)
    player_x += 3
    name_x += 3
    stdscr.addstr(name_y - 2, name_x, name_profile)
    stdscr.addstr(player_y - 2, player_x, "🦖")
    stdscr.refresh()
    time.sleep(0.035)
    stdscr.addstr(name_y - 2, name_x, " " * len(name_profile))
    stdscr.addstr(player_y - 2, player_x, " ")
    stdscr.refresh()
    time.sleep(0.035)
    stdscr.addstr(name_y, name_x, name_profile)
    stdscr.addstr(player_y, player_x, "🦖")
    stdscr.refresh()
    return game_control(stdscr, name_profile, player_x, player_y, name_x, name_y, max_width)
    
    