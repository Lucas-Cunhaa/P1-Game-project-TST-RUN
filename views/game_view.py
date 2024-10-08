def game_view(stdscr, name_profile):
    from assests.logo import name_game
    from assests.logo import profile_image
    from controllers.game_control import game_control

    stdscr.clear()

    max_height, max_width = stdscr.getmaxyx()

    lines = "_" * (max_width - 2)
    fire = "🔥" * ((max_width - 2) // 2)
    y = max_height - 2
    x = 1
    start_x = (len(name_profile) // 2) - 1
    start_y = y - 2

    stdscr.addstr(x, x, name_game) # logo name
    stdscr.addstr(start_y - 3, x, name_profile) # nema_profile
    stdscr.addstr(start_y, start_x, "🦖") # player_person
    stdscr.addstr(y, x, lines) # floor
    stdscr.addstr(y + 1, x, fire) # fire of the game

    stdscr.refresh()

    game_control(stdscr, name_profile, start_x, start_y, x, max_width)
        
        
       