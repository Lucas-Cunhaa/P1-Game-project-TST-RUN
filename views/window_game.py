import curses

def game_window(stdscr, win, name_profile):
    from .window_home import home_page
    stdscr.clear()
    stdscr.refresh()
    win.clear()
    win.box()
    win.addstr(1, 1, f"Your profile: {name_profile}")
    win.addstr(2, 1, "Press 'enter' to start the game")
    win.refresh()

    KEY_ESC = 27 
    KEY_ENTER = 10
    while True:
        key = stdscr.getch()
        if key == KEY_ESC: return home_page(stdscr, name_profile, start_game= False)
        if key == KEY_ENTER: return home_page(stdscr, name_profile, start_game= True)



