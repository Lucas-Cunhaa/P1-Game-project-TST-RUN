import time 

def left(stdscr, name_profile, player_x, player_y, name_x, name_y, max_height, max_width):
    from controllers.game_control import game_control
    stdscr.addstr(player_y, player_x[0], " ")
    stdscr.addstr(name_y, name_x[0], " " * len(name_profile))
    if player_x[0] - 5 > 75:
        player_x[0] -= 5
        name_x[0] -= 5
    stdscr.addstr(player_y, player_x[0], "🤓")
    stdscr.addstr(name_y, name_x[0], name_profile)
    stdscr.refresh()
    # return game_control(stdscr, name_profile, player_x, player_y, name_x, name_y, max_height, max_width)