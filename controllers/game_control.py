import time
import curses

interval = 0.5
def game_control(stdscr, name_profile, player_x, player_y, name_x, name_y, max_width):
    from .comands.jump import jump 
    from .comands.left import left
    from .comands.right import right
    global interval
    KEY_SPACE = 32
    stdscr.keypad(True) 
    stdscr.nodelay(True)
    obj = "🪵"
    subt = 3
    while True:
        stdscr.addstr(player_y, max_width - 1, "  ")
        time.sleep(interval)
        max_width -= subt
        stdscr.addstr(player_y, max_width - 1, "🪵")
        stdscr.refresh()
    
        key = stdscr.getch()
        
        if key == KEY_SPACE: jump(stdscr, name_profile, player_x, player_y, name_x, name_y, max_width)
        if key == curses.KEY_LEFT: left(stdscr, name_profile, player_x, player_y, name_x, name_y, max_width) 
        if key == curses.KEY_RIGHT: right(stdscr, name_profile, player_x, player_y, name_x, name_y, max_width)
        stdscr.refresh()

        if interval > 0.25: interval = interval * 0.95
        if player_x == max_width: break

    
