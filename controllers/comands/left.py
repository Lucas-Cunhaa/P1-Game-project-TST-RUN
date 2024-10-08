import time 

def left(stdscr, name_profile, player_x, player_y, name_x, max_width):
    from controllers.game_control import game_control
    stdscr.addstr(player_y, player_x, " ")
    time.sleep(0.02)
    player_x -= 1
    stdscr.addstr(player_y, player_x, "🦖")
    stdscr.refresh()
    return game_control(stdscr, name_profile, player_x, player_y, name_x, max_width)