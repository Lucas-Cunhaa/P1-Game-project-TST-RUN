import curses

def text(win, mensage, stdscr): 
    from views.window_home import home_page
    from views.window_profile import window_profile
    text = ""
    while True:
        win.clear() 
        win.box()
        win.addstr(1, 1, mensage, curses.color_pair(1))
        win.addstr(1, len(mensage) + 1, text, curses.color_pair(1))
        win.refresh()

        key = win.getch() 
        
        KEY_ESC = 27
        KEY_BACKSPACE = 8
        KEY_ENTER = 10
        if key == KEY_ESC: 
            return home_page(stdscr)
        elif key == KEY_BACKSPACE:
            text = text[:-1]
        elif key == KEY_ENTER: 
            break
        else:
            # Adiciona a tecla pressionada ao perfil, se não for um caractere de controle
            if chr(key).isprintable():
                text += chr(key)

    return text