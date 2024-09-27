import curses

def interface1(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Interface 1") # mensagem
    stdscr.addstr(1, 0, "Pressione 'n' para ir para a Interface 2")
    stdscr.refresh()
    while True:
        key = stdscr.getch()  # pega a tecla utilizada
        if key == ord('n'):   # verifica se a tecla é 'n'
            break  # sai do loop para voltar ao mai

def main(stdscr):
    KEY_ENTER = 10
    stdscr.clear()
    stdscr.addstr("Hello, Curses!")
    stdscr.addstr(2, 0, "Pressione Enter para ir para a Interface 1")
    stdscr.refresh()
    while True: 
        key = stdscr.getch() # pega a tecla utilizada
        if key == KEY_ENTER: 
            interface1(stdscr)
            break

curses.wrapper(main)
