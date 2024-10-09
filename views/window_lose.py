import curses
import time 

def lose_window(stdscr, win, name_profile):
    from .window_home import home_page
    from assets.jorge import jorge

    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

    stdscr.clear()
    win.box()

    x, y = 1, 1
    jorge_start_x = 5
    jorge_start_y = 5

    delay = 0.1
    text_window = f"You were impugned by jorge.py {name_profile}"
    
    for char in text_window:
        stdscr.addch(y, x, char, curses.color_pair(1))
        stdscr.refresh()
        time.sleep(delay)  

    stdscr.addstr(jorge_start_y, jorge_start_x, jorge)
    win.addstr(5, 5, "Press 'enter' to restart the game")
    win.refresh()
    
    KEY_ENTER = 10
    while True:
        key = win.getch()
        start_game = True if key == KEY_ENTER else False
        return home_page(stdscr, name_profile, start_game)
        #if key == KEY_ENTER: return (stdscr, name_profile, start_game= True)



