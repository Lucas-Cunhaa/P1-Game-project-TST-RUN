import curses
import time 

def lose_window(stdscr, name_profile):
    from .window_home import home_page
    from assets.jorge import jorge
    from controllers.display_ascci_image import display_ascii
    from controllers.display_text import display_text
    from controllers.restart_options import restart_options

    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.clear()

    jorge_x = 1
    jorge_y = 1
    display_ascii(stdscr, jorge_y, jorge_x, jorge, 1)

    end_game_text = f"Hey {name_profile}, you were impugned by jorge.py 😈"
    width = len(end_game_text) + 4
    height = 10  
    max_height, max_width = stdscr.getmaxyx()
    start_y = (max_height - height) // 2  
    start_x = (max_width - width) // 2
    
    win = curses.newwin(height, width, start_y, start_x)
    win.box()

    end_text_x,  end_text_y = 1, 1
    delay = 0.06
    display_text(win, end_text_y,  end_text_x, end_game_text, delay, 1)

    restart_options(win, height, width)
    
    KEY_ENTER = 10
    KEY_ESC = 27
    while True:
        key = win.getch()
        if key == KEY_ENTER:
            start_game = True  
            return home_page(stdscr, name_profile, start_game)  
        if key == KEY_ESC: return "__finish__"

 



