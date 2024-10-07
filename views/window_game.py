import curses

def game_window(stdscr, win, name_profile):
    from .window_home import home_page
    stdscr.clear()
    stdscr.refresh()
    win.clear()
    win.box()
    win.addstr(1, 1, f"Your profile: {name_profile}")
    win.addstr(2, 1, "ola")
    win.refresh()

    ESC = 27 
    while True:
        key = stdscr.getch()
        if key == ESC: return home_page(stdscr, name_profile)
        



