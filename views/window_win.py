import curses

def win_window(stdscr,name_profile):
    from .window_home import home_page
    from assets.dalton_win import dalton_win
    from controllers.display_ascci_image import display_ascii
    from controllers.display_text import display_text
    from controllers.restart_options import restart_options
    
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)

    stdscr.clear()

    dalton_win_x = 1
    dalton_win_y = 1
    display_ascii(stdscr, dalton_win_y, dalton_win_x, dalton_win, 1)
    
    win_text = f"Hey {name_profile}, you’ve completed all first-semester Computer Science units at UFCG and defeated Jorge.py!"
    width = len(win_text) + 4
    height = 10  
    max_height, max_width = stdscr.getmaxyx()

    start_y = (max_height - height) // 2  
    start_x = (max_width - width) // 2
    
    win = curses.newwin(height, width, start_y, start_x)
    win.box()

    win_text_x,win_text_y = 1, 1
    delay = 0.06
    display_text(win,win_text_y, win_text_x, win_text, delay, 1)

    restart_options(win, height, width)

    KEY_ENTER = 10
    KEY_ESC = 27
    while True:
        key = win.getch()
        if key == KEY_ENTER:
            start_game = True  
            return home_page(stdscr, name_profile, start_game)  
        if key == KEY_ESC: return "__finish__"
