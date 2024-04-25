#!/bin/python3
import curses, sys

def setup():
    curses.raw()
    curses.noecho()

    # init screen
    screen = curses.initscr()
    screen.keypad(1) # enable keypad
    screen.nodelay(1)
    return screen

def readFile():
    buffer = []
    # get filename
    filename = 'file.txt'
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    # try to open file, checks for existence
    try:
        with open(filename) as file:
            # get file contents line by line
            content = file.read().split('\n')
            # remove the last line, unless it's the first line
            if (len(content) > 1):
                content = content[:-1]
            # add ascii values for each char in row to buffer
            for row in content:
                buffer.append([ord(char) for char in row])
            return filename, buffer
    except:
        # create file, return empty string as content
        buffer.append([])
        return filename, buffer


def main(stdscr):
    # get screen (s)
    screen = setup()
    rows, cols = screen.getmaxyx()
    x, y, row, col = 0, 0, 0, 0

    # parse arg, read file
    src, buffer = readFile()

    while True:
        char = -1 # if no key press, screen.getch() return -1
        while (char == -1):
            char = screen.getch()
        if char == (ord('q') & 0x1f):
            # checks for ctrl + q
            sys.exit()

curses.wrapper(main)
