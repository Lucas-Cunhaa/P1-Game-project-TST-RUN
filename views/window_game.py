import curses

def game_window(stdscr, win):
    from index import home_page
    stdscr.clear()
    stdscr.refresh()
    win.clear()

    ESC = 27 
    while True:
        key = stdscr.getch()
        if key == ESC: return home_page(stdscr)
        



