def game(stdscr, name_profile):
    from views.logo import name_game
    stdscr.clear()
    max_height, max_width = stdscr.getmaxyx()
    lines = "_" * (max_width - 2)
    fire = "🔥" * (max_width - 2)
    y = int(max_height / 1.15)
    x = 1
    stdscr.addstr(x, x, name_game)
    stdscr.addstr(y - 5, x, name_profile)
    stdscr.addstr(y - 4, x, lines)
    stdscr.addstr(y, x, lines)
    stdscr.addstr(y + 1, x, fire)
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        # if key == KEY_SPACE: jump()
        
        
       