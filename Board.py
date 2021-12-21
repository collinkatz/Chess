from graphics import *


class Board:
    spaces = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ]

    def __init__(self):
        self.spaces[1][2] = None


def main():
    win = GraphWin("game", 1080, 1080)
    c = Circle(Point(50, 50), 10)
    c.draw(win)
    win.getMouse()  # Pause to view result
    win.close()  # Close window when done


main()
