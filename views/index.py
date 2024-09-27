import curses
from window_profile import profile_window 
# from window_game import game_window 

def home_page(stdscr):
    profile_window(stdscr)
    # game_window(stdscr) 
    
def main(stdscr):
    home_page(stdscr)
    # start_game(stdscr)
     
curses.wrapper(main)