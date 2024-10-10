import curses

def game_view(stdscr, name_profile):
    from assets.logo import name_game
    from assets.logo import profile_image
    from assets.wilkerson import wilkerson
    from controllers.game_control import game_control
    from controllers.display_ascci_image import display_ascii

    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    stdscr.clear()

    max_height, max_width = stdscr.getmaxyx()

    x = 75
    lines = "_" * ((max_width - 2) - x + 2)
    fire = "🔥" * (((max_width - 2) // 2) - x)
    y = max_height - 2
    start_x = (len(name_profile) // 2) + x  - 2
    start_y = y - 1

    stdscr.addstr(1, 1, name_game) # logo name
    stdscr.addstr(start_y - 3, x, name_profile) # name_profile

    wilkerson_start_x = 1 
    wilkerson_start_y = 9
<<<<<<< HEAD
    stdscr.addstr(wilkerson_start_y,  wilkerson_start_x, wilkerson)  #  wilkerson
    stdscr.addstr(y, 1, "0x ✅")
=======
    display_ascii(stdscr, wilkerson_start_y, wilkerson_start_x, wilkerson, 1)

>>>>>>> 1e5e60bbee857ba0d62986e959f8d1295573acea
    stdscr.addstr(start_y, start_x, "🤓") # player_person

    for i in range(y):
        stdscr.addstr(i, x - 1, "|") #  wall1
        stdscr.addstr(i, max_width - 1, "|") # wall2

    stdscr.addstr(y, x, lines) # floor
    stdscr.addstr(y + 1, x, fire) # fire of the game

    stdscr.refresh()

    game_control(stdscr, name_profile, start_x, start_y, x, start_y - 3, max_height, max_width)


