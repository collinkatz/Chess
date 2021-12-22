from graphics import *
from Piece import *
import math


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
        self.spaces[1][2] = Pawn((1, 2), "Black")

    def draw_board(self):
        drawn_spaces = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ]
        drawn_pieces = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ]
        for row in range(len(self.spaces)):
            for column in range(len(self.spaces[row])):
                square = Rectangle(Point(column * 50, row * 50), Point(column * 50 - 50, row * 50 - 50))
                if pow(-1, row + column) == 1:
                    square.setFill("White")
                else:
                    square.setFill("Black")
                drawn_spaces[row][column] = square
        for row in range(len(self.spaces)):
            for column in range(len(self.spaces[row])):
                piece = self.spaces[row][column]
                if piece == "black_pawn":
                    drawn_pieces[row][column] = Image(Point(column * 50, row * 50), "")
                elif piece == "white_pawn":

                elif piece == "black_bishop":

                elif piece == "white_bishop":

                elif piece == "black_knight":

                elif piece == "white_knight":

                elif piece == "black_rook":

                elif piece == "white_rook":

                elif piece == "black_queen":

                elif piece == "white_queen":

                elif piece == "black_king":

                elif piece == "white_king":

        return drawn_spaces, drawn_pieces


def main():
    win = GraphWin("game", 1080, 1080)
    # c = Circle(Point(50, 50), 10)
    # c.draw(win)
    board = Board()
    spaces = board.draw_board()
    for row in range(len(spaces)):
        for space in range(len(spaces[row])):
            spaces[row][space].draw(win)
    win.getMouse()  # Pause to view result
    win.close()  # Close window when done



main()
