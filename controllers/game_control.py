import time
import curses

def game_control(stdscr, name_profile, player_x, player_y, name_x, max_width):
    from .comands.jump import jump 
    from .comands.left import left
    from .comands.right import right
    KEY_SPACE = 32
    stdscr.keypad(True) 
    stdscr.nodelay(True)
    while True:
        key = stdscr.getch()
        
        if key == KEY_SPACE: jump(stdscr, name_profile, player_x, player_y, name_x, max_width)
        elif key == curses.KEY_LEFT: left(stdscr, name_profile, player_x, player_y, name_x, max_width) 
        elif key == curses.KEY_RIGHT: right(stdscr, name_profile, player_x, player_y, name_x, max_width)
        stdscr.refresh()
    
    