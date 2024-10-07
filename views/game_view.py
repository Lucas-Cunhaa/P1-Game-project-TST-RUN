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

    stdscr.addstr(x, x, name_game)
    stdscr.addstr(y - 5, x, name_profile)
    stdscr.addstr(y - 2, start_x, "🦖")
    stdscr.addstr(y, x, lines)
    stdscr.addstr(y + 1, x, fire)

    stdscr.refresh()

    game_control(stdscr, name_profile, profile_image, start_x, x, y, max_width)
        
        
       