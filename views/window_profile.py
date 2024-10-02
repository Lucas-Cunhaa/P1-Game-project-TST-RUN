import curses

def window_profile(stdscr, win):
    from index import home_page
    stdscr.clear()
    stdscr.refresh()
    win.clear()
    win.box()
    
    win.addstr(1, 1, "Your profile")
    win.addstr(2, 1, "Change your avatar")
    win.addstr(3, 1, "Change your name")
    win.refresh()
     
    esc = 27
    while True:
        key = win.getch()
        if key == esc:
            home_page(stdscr)
            break 

