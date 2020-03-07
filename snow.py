import curses
from time import sleep
from random import randint

screen = curses.initscr()
max_rows, max_columns = screen.getmaxyx()
curses.curs_set(0)
curses.noecho()
screen.timeout(100)
snowflakes = []

#screen.addstr(0, 30, "")



while True:
    row = 0
    column = randint(0, max_columns -2)
    snowflakes.append((row, column))
    screen.clear()

    iceflakes = []
    for row, column in snowflakes:
        screen.addch(row, column, "*")
        if row < max_rows - 2:
            row += 1
        else:
            row = 0
            column = randint(0, max_columns -2)
        iceflakes.append((row,column))

    #switching snowflakes and iceflakes
    snowflakes = iceflakes

    if screen.getch() == 3:
        exit()

