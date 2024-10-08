import curses
from views.window_home import home_page
from views.game_view import game_view


def main(stdscr):
    name_profile = "Dalton (DEFAULT)"
    name_profile = home_page(stdscr, name_profile, start_game= False)
    return game_view(stdscr, name_profile)
     
curses.wrapper(main)