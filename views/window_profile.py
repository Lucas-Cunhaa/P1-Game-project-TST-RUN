import curses

def window_profile(stdscr, win):
    from index import home_page
    stdscr.clear()
    stdscr.refresh()
    win.clear()
    win.box()
    
    # Configurações de cor
    curses.start_color()  # Inicializa o uso de cores
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Texto branco, fundo preto

    mensage = "Your profile: > "
    win.addstr(1, 1, mensage, curses.color_pair(1))
    win.refresh() 
    profile = win.getstr(1, len(mensage)).decode('utf-8')
    win.addstr(3, 1, f"Name Profile: {profile}", curses.color_pair(1))
    win.addstr(4, 1, "Change your avatar", curses.color_pair(1))
    win.addstr(5, 1, "Change your name", curses.color_pair(1))
    win.refresh()
     
    esc = 27
    while True:
        key = win.getch()
        if key == esc: return home_page(stdscr)
             

