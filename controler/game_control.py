import time

def game_control(stdscr, name_profile, player, player_x, name_x, y, max_width):
    from .jump import jump 
    KEY_SPACE = 32
    stdscr.nodelay(True)
    interval = 0.70
    while True:
        stdscr.addstr(y - 2, player_x, " ")

        time.sleep(interval)
        if interval > 0.30: interval *= 0.95

        player_x += 1
        stdscr.addstr(y - 2, player_x, "🦖")
        key = stdscr.getch()

        if key == KEY_SPACE: return jump(stdscr, name_profile, player, player_x, name_x, y, max_width)

        stdscr.refresh()
    