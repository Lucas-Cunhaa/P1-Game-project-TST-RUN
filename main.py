import curses
from views.window_home import home_page
from views.game_view import game_view

def main(stdscr):
    name_profile = "Dalton (DEFAULT)"
    home_page(stdscr, name_profile, start_game= False)
    game_view(stdscr, name_profile)
     
curses.wrapper(main)