import curses

def window_profile(stdscr, win, name_profile):
    from .window_home import home_page
    from controler.name_profile import new_name
    stdscr.clear()
    stdscr.refresh()
    win.clear()
    win.box()
    
    mensage = "Your profile: > " 
    new_name = new_name(win, mensage, stdscr, name_profile)
    if new_name.isprintable() and new_name != "": name_profile = new_name
    win.addstr(3, 1, f"Name Profile: {name_profile}")
    win.addstr(4, 1, "Change your avatar")
    win.addstr(5, 1, "Change your name")
    win.refresh()
    
    ESC = 27 
    while True:
        key = win.getch()
        if key == ESC: return home_page(stdscr, name_profile, start_game= False)