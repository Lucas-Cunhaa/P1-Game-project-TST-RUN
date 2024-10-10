import curses

def display_ascii(stdscr, x, y, image, color):
    try:
        stdscr.addstr(y, x, image, curses.color_pair(color))
        stdscr.refresh()
    except curses.error as e:
        stdscr.refresh()

