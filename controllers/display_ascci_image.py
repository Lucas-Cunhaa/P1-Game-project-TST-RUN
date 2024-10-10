import curses

def display_ascii(stdscr, x, y, image, color):
    stdscr.addstr(y, x, image, curses.color_pair(color))
    stdscr.refresh()
