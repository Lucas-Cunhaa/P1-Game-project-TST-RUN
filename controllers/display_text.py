import curses 
import time 

def display_text(win, y, x, text, delay, color):
    i = 0
    for char in text:
        win.addch(y, x + i, char, curses.color_pair(color))
        win.refresh()
        time.sleep(delay) 
        i += 1