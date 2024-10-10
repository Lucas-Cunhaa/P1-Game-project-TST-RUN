import time
import curses
import sys
import random

NUM_X = int(sys.argv[1] if len(sys.argv) > 1 else 50)

def chuva_x(stdscr, chuva_obj, max_height):
    for X in chuva_obj:
        line = X[0]
        col = X[1]
        try: 
            if line < max_height - 3:
                stdscr.addstr(line, col, "❌")
        except:
            raise(Exception(str(locals())))
        stdscr.refresh()
        
    time.sleep(0.05)
    for X in chuva_obj:
        line = X[0]
        col = X[1]
        stdscr.addstr(line, col, " ")
        stdscr.refresh()
        if line < max_height - 3:
            X[0] += 1
        else:
            X[0] = 0

def game_control(stdscr, name_profile, player_x, player_y, name_x, name_y, max_height, max_width):
    from views.window_lose import lose_window
    from .comands.jump import jump 
    from .comands.left import left
    from .comands.right import right

    KEY_SPACE = 32
    stdscr.keypad(True) 
    stdscr.nodelay(True)
    # obj = "❌"
    chuva_obj = []
    player_x = [player_x]
    name_x = [name_x]

    while True:
        key = stdscr.getch()
        
        if key == KEY_SPACE: jump(stdscr, name_profile, player_x, player_y, name_x, name_y, max_height, max_width)
        if key == curses.KEY_LEFT: left(stdscr, name_profile, player_x, player_y, name_x, name_y, max_height, max_width) 
        if key == curses.KEY_RIGHT: right(stdscr, name_profile, player_x, player_y, name_x, name_y, max_height, max_width)

        chuva_x(stdscr, chuva_obj, max_height)
        if len(chuva_obj) < NUM_X:
            lin, col = 0, random.randint(75, max_width - 3)
            chuva_obj.append([lin, col])
        stdscr.refresh()
        # return lose_window(stdscr, name_profile)
        

    
