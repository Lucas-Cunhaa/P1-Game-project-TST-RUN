import curses
from views.window_home import home_page
from views.game_view import game_view


def main(stdscr):
    name_profile = "Dalton (DEFAULT)"
    while True:
        name_profile = home_page(stdscr, name_profile, start_game= False)
        result = game_view(stdscr, name_profile)
        if result == "__finish__": break
        
    print("You have finished the TST RUN")
     
curses.wrapper(main)