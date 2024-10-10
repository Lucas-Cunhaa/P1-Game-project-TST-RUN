import curses

def home_page(stdscr, name_profile, start_game):
    from .window_profile import window_profile 
    from .window_game import game_window 
    from controllers.display_ascci_image import display_ascii
    from controllers.display_text import display_text
    from assets.dalton import dalton

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    if start_game == True: return name_profile
    stdscr.clear()
    
    max_height, max_width = stdscr.getmaxyx()

    dalton_start_x = 1
    dalton_start_y = 1
    display_ascii(stdscr, dalton_start_y, dalton_start_x, dalton, 1)

    height = 10 
    width = 40   
    start_y = (max_height - height) // 2  
    start_x = (max_width - width) // 2
    
    win = curses.newwin(height, width, start_y, start_x)
    
    win.box()

    win.addstr(1, 1, "GAME: TST-RUN")
    win.addstr(3, 1, "Press '1' to the window_game")
    win.addstr(4, 1, "Press '2' to change profile")

    game_credits = "Created by Lucas Cunha and Joao Neto"
    delay = 0.08
    display_text(win, 8, 1, game_credits, delay, 1)
    win.addstr(8, 1, "Created by Lucas Cunha and Joao Neto")
    win.refresh()
    
    KEY_1 = 49
    KEY_2 = 50
    while True: 
        key = win.getch()
        if key == KEY_2: return window_profile(stdscr, win, name_profile)
        if key == KEY_1: return game_window(stdscr, win, name_profile)   
