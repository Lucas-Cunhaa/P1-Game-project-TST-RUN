import time
import curses
import sys
import random

NUM_X = int(sys.argv[1] if len(sys.argv) > 1 else 100)

def rain_x(stdscr, rain_obj, max_height, tokens, interval):
    for X in rain_obj:
        line = X[0]
        col = X[1]
        try: 
            if line < max_height - 3 and (line, col) not in tokens:
                stdscr.addstr(line, col, "❌")
        except:
            raise(Exception(str(locals())))
                        
        stdscr.refresh()
        
    if interval[0] > 0.07: interval[0] *= 0.99 
    time.sleep(interval[0])
    for X in rain_obj:
        line = X[0]
        col = X[1]
        stdscr.addstr(line, col, " ")
        stdscr.refresh()
        if line < max_height - 3 and (line + 1, col) not in tokens:
            X[0] += 1
        else:
            X[0] = 0

def game_control(stdscr, name_profile, player_x, player_y, name_x, name_y, max_height, max_width):
    from views.window_win import win_window
    from views.window_lose import lose_window
    from .comands.jump import jump 
    from .comands.left import left
    from .comands.right import right
    
    interval = 0.15
    KEY_SPACE = 32
    stdscr.keypad(True) 
    stdscr.nodelay(True)
    rain_obj = []
    tokens = {}
    interval = [interval]
    player_x = [player_x]
    name_x = [name_x]
    p1_test = 0
    

    while True:
        key = stdscr.getch()
        
        if key == KEY_SPACE: jump(stdscr, name_profile, player_x, player_y, name_x, name_y, max_height, max_width)
        if key == curses.KEY_LEFT: left(stdscr, name_profile, player_x, player_y, name_x, name_y, max_height, max_width) 
        if key == curses.KEY_RIGHT: right(stdscr, name_profile, player_x, player_y, name_x, name_y, max_height, max_width)

        rain_x(stdscr, rain_obj, max_height, tokens, interval)
        for X in rain_obj:
            if (player_y - 1 <= X[0] <= player_y + 1) and (player_x[0] - 1 <= X[1] <= player_x[0] + 1):
                return lose_window(stdscr, name_profile)
            
        for T in tokens:
            if (player_y - 1 <= T[0] <= player_y + 1) and (player_x[0] - 1 <= T[1] <= player_x[0] + 1):
                p1_test += 1
                stdscr.addstr(T[0], T[1], " ")
                tokens.pop(T)
                break
                
        if len(rain_obj) < NUM_X:
            lin, col = 0, random.randrange(75, max_width - 3, 5)
            rain_obj.append([lin, col])

        while len(tokens) < 2:
            line_check, col_check = player_y, random.randrange(75, max_width - 3, 5)
            place = (line_check, col_check)
            if place not in tokens: 
                tokens[place] = "✅"
                stdscr.addstr(place[0], place[1], "✅")
        
        text_tokens = f"{p1_test // 2} UNIT ✅"
        stdscr.addstr(player_y, 70 - len(text_tokens), text_tokens)
        if p1_test == 20: return win_window(stdscr, name_profile)
        stdscr.refresh()
        
        

    
