import curses


def window_profile(stdscr):
    from index import home_page
    stdscr.clear()

    stdscr.addstr(0, 0, "Your profile") 
    stdscr.addstr(1, 0, "Change your avatar")
    stdscr.addstr(2, 0, "Change your name")

    stdscr.refresh()

    esc = 10
    while True:
        key = stdscr.getch()
        if key == esc:
            home_page(stdscr)
            break 

