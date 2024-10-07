import curses
from views.window_home import home_page
from controler.game import game

def main(stdscr):
    name_profile = "Dalton (DEFAULT)"
    home_page(stdscr, name_profile, start_game= False)
    game(stdscr, name_profile)
     
curses.wrapper(main)