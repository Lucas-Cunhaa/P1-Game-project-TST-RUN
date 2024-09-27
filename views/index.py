import curses
import profile_window from window.py
import game_window from window.py

def home_page(stdscr):
    profile_window(stdscr)
    game_window(stdscr) 
    
def main(stdscr):
    home_page(stdscr)
    start_game(stdscr)
     
curses.wrapper(main)