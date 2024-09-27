import curses
import home_page from index.py
def profile_window(stdscr):
    stdscr.clear()

    stdscr.addstr(0, 0, "Your profile") 
    stdscr.addstr(1, 0, "Change your avatar")
    stdscr.addstr(1, 0, "Change your name")

    stdscr.refresh()

    esc = curses.KEY_ESC
    while True:
        key = stdscr.getch()
        if key == esc:
            home_page(stdscr)
            break 

