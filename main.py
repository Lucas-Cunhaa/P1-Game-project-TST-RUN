import curses
from views.window_home import home_page 

def main(stdscr):
    home_page(stdscr)
    # start_game(stdscr)
     
curses.wrapper(main)