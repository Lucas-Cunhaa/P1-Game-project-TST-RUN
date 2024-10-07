import curses
from views.window_home import home_page 

def main(stdscr):
    name_profile = "Dalton (DEFAULT)"
    home_page(stdscr, name_profile, start_game= False)
    # start_game(stdscr)
     
curses.wrapper(main)