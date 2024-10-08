import curses

def game_view(stdscr, name_profile):
    from assets.logo import name_game
    from assets.logo import profile_image
    from assets.jorge import jorge
    from assets.wilkerson import wilkerson
    from controllers.game_control import game_control
    
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    stdscr.clear()

    max_height, max_width = stdscr.getmaxyx()

    lines = "_" * (max_width - 2)
    fire = "🔥" * ((max_width - 2) // 2)
    y = max_height - 2
    x = 1
    start_x = (len(name_profile) // 2) - 1
    start_y = y - 2

    stdscr.addstr(x, x, name_game) # logo name
    stdscr.addstr(start_y - 3, x, name_profile) # name_profile
    
    jorge_start_x = 1 
    jorge_start_y = 9
    stdscr.addstr(jorge_start_y, jorge_start_x, jorge)  # jorge

    stdscr.addstr(start_y, start_x, "🤓") # player_person
    stdscr.addstr(y, x, lines) # floor
    stdscr.addstr(y + 1, x, fire) # fire of the game
    stdscr.addstr(start_y, max_width - 1, "❌")

    stdscr.refresh()

    game_control(stdscr, name_profile, start_x, start_y, x, start_y - 3, max_width)


    