import time

def jump(stdscr, name_profile, player, player_x, name_x, y, max_width):
    from .game_control import game_control
    stdscr.addstr(y - 2, player_x, " ")
    time.sleep(0.05)
    stdscr.addstr(y - 4, player_x, "🦖")
    stdscr.refresh()
    time.sleep(0.05)
    stdscr.addstr(y - 4, player_x, " ")
    time.sleep(0.05)
    player_x += 3
    stdscr.addstr(y - 4, player_x, "🦖")
    stdscr.refresh()
    time.sleep(0.05)
    stdscr.addstr(y - 4, player_x, " ")
    stdscr.refresh()
    time.sleep(0.05)
    stdscr.addstr(y - 2, player_x, "🦖")
    stdscr.refresh()
    return game_control(stdscr, name_profile, player, player_x, name_x, y, max_width)