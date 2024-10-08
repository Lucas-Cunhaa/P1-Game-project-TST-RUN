import curses

def new_name(win, mensage, stdscr, name_profile): 
    from views.window_home import home_page
    new_name = ""
    while True:
        win.clear() 
        win.box()
        win.addstr(1, 1, mensage)
        win.addstr(1, len(mensage) + 1, new_name)
        win.refresh()

        key = win.getch()
    
        KEY_ESC = 27
        KEY_BACKSPACE = 8
        KEY_ENTER = 10
        if key == KEY_ESC: 
            return home_page(stdscr, name_profile, start_game= False)
        elif key == KEY_BACKSPACE:
            new_name = new_name[:-1]
        elif key == KEY_ENTER: 
            return new_name
        else:
            if chr(key).isprintable():
                new_name += chr(key)
    