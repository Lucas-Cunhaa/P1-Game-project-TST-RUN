import curses
from window_profile import window_profile 
# from window_game import game_window 

def home_page(stdscr):
    stdscr.clear()

    stdscr.addstr(0, 0, "GAME: TST-RUN")
    stdscr.addstr(1, 0, "Press '1' to start the game")
    stdscr.addstr(2, 0, "Press '2' to change profile")

    stdscr.refresh()
    KEY_1 = 49
    KEY_2 = 50
    while True: 
        key = stdscr.getch()
        if key == KEY_2: window_profile(stdscr)
    # elif key == KEY_1: game_window(stdscr) 
    
def main(stdscr):
    home_page(stdscr)
    # start_game(stdscr)
     
curses.wrapper(main)