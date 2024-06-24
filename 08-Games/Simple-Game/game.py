import curses

def main(stdscr):
    stdscr.clear()
    screen_height, screen_width = stdscr.getmaxyx()

    x = screen_width // 2
    y = screen_height // 2

    while True:
        stdscr.addstr(y, x, 'X')
        key = stdscr.getch()
        stdscr.addstr(y, x, ' ')
        if key == ord('q'):
            break
        if key == curses.KEY_UP and y > 0:
            y = y - 1
        if key == curses.KEY_DOWN and y < screen_height - 1:
            y = y + 1
        if key == curses.KEY_LEFT and x > 0:
            x = x - 1
        if key == curses.KEY_RIGHT and x < screen_width - 2:
            x = x + 1

curses.wrapper(main)
