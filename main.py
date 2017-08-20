#!/usr/bin/python3

from graphics import *

from board import Board

SQUARE_SIZE = 20

BOARD_WIDTH = 10
BOARD_HEIGHT = 10


def main():
    width = BOARD_WIDTH * SQUARE_SIZE
    height = BOARD_HEIGHT * SQUARE_SIZE

    win = GraphWin("Game of Life", width, height, autoflush=False)

    b = Board(win, BOARD_WIDTH, BOARD_HEIGHT)
    b.draw()
    win.update()

    win.getMouse()
    win.close()

main()
