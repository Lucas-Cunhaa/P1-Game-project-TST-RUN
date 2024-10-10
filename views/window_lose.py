import curses
import time 

def lose_window(stdscr, name_profile):
    from .window_home import home_page
    from assets.jorge import jorge
    from controllers.display_ascci_image import display_ascii
    from controllers.display_text import display_text

    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.clear()

    jorge_x = 1
    jorge_y = 1
    display_ascii(stdscr, jorge_y, jorge_x, jorge, 1)

    text_window = f"Hey {name_profile}, you were impugned by jorge.py 😈"
    width = len(text_window) + 4
    height = 10  
    max_height, max_width = stdscr.getmaxyx()
    
    start_y = (max_height - height) // 2  
    start_x = (max_width - width) // 2
    
    win = curses.newwin(height, width, start_y, start_x)
    win.box()

    x, y = 1, 1
    delay = 0.06
    display_text(win, y, x, text_window, delay, 1)
    win.refresh()
    text = "Press 'enter' to restart the game"
    x_text = (width // 2) - (len(text) // 2)
    y_text = height // 2
    win.addstr(y_text, x_text, text)
    win.refresh()

    KEY_ENTER = 10
    KEY_ENTER = 10
    while True:
        key = win.getch()
        if key == KEY_ENTER:
            start_game = True  
            return home_page(stdscr, name_profile, start_game)  

 



