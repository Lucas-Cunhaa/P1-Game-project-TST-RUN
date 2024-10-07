import curses

def window_profile(stdscr, win):
    from .window_home import home_page
    from controler.text import text
    stdscr.clear()
    stdscr.refresh()
    win.clear()
    win.box()
    
    # Configurações de cor
    curses.start_color()  # Inicializa o uso de cores
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Texto branco, fundo preto

    mensage = "Your profile: > " 
    profile = text(win, mensage, stdscr)
    win.addstr(3, 1, f"Name Profile: {profile}", curses.color_pair(1))
    win.addstr(4, 1, "Change your avatar", curses.color_pair(1))
    win.addstr(5, 1, "Change your name", curses.color_pair(1))
    win.refresh()
     
    win.getch()