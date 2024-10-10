def restart_options(win, height, width):
    restart_text = "Press 'enter' to restart the game"
    restart_text_x  = (width // 2) - (len(restart_text) // 2)
    restart_text_y = height // 2
    win.addstr(restart_text_y,  restart_text_x, restart_text)

    finish_text = "Press 'esc' to finish the game"
    win.addstr(restart_text_y + 1, restart_text_x + 2, finish_text)

    win.refresh()