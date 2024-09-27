import curses
from window_profile import window_profile 
# from window_game import game_window 

def home_page(stdscr):
    window_profile(stdscr)
    # game_window(stdscr) 
    
def main(stdscr):
    home_page(stdscr)
    # start_game(stdscr)
     
curses.wrapper(main)