import time

def jump(stdscr, name_profile, player_x, player_y, name_x, name_y, max_height, max_width):
    from controllers.game_control import game_control
    stdscr.addstr(name_y, name_x[0], " " * len(name_profile))
    stdscr.addstr(player_y, player_x[0], " ")
    time.sleep(0.005)
    stdscr.addstr(name_y - 2, name_x[0], name_profile)
    stdscr.addstr(player_y - 2, player_x[0], "🤓")
    stdscr.refresh()
    time.sleep(0.005)
    stdscr.addstr(name_y - 2, name_x[0], " " * len(name_profile))
    stdscr.addstr(player_y - 2, player_x[0], " ")
    time.sleep(0.025)
    if player_x[0] + 5 < max_width: 
        player_x[0] += 5
        name_x[0] += 5
    stdscr.addstr(name_y - 2, name_x[0], name_profile)
    stdscr.addstr(player_y - 2, player_x[0], "🤓")
    stdscr.refresh()
    time.sleep(0.005)
    stdscr.addstr(name_y - 2, name_x[0], " " * len(name_profile))
    stdscr.addstr(player_y - 2, player_x[0], " ")
    stdscr.refresh()
    time.sleep(0.005)
    stdscr.addstr(name_y, name_x[0], name_profile)
    stdscr.addstr(player_y, player_x[0], "🤓")
    stdscr.refresh()
    
    
    