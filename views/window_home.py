import curses

def home_page(stdscr, name_profile, start_game):
    from .window_profile import window_profile 
    from .window_game import game_window 
    if start_game == True: return
    stdscr.clear()
    
    max_height, max_width = stdscr.getmaxyx()

    height = 10 
    width = 40   
    start_y = (max_height - height) // 2  
    start_x = (max_width - width) // 2
    
    win = curses.newwin(height, width, start_y, start_x)
    
    win.box()

    win.addstr(1, 1, "GAME: TST-RUN")
    win.addstr(3, 1, "Press '1' to the window_game")
    win.addstr(4, 1, "Press '2' to change profile")
    win.refresh()
    
    KEY_1 = 49
    KEY_2 = 50
    while True: 
        key = win.getch()
        if key == KEY_2: return window_profile(stdscr, win, name_profile)
        if key == KEY_1: return game_window(stdscr, win, name_profile)    