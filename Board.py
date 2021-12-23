from graphics import *
from Piece import *
import math
import os.path as path


class Board:
    SQUARE_SIZE = 100
    PIECE_IMAGES = "resources/pieces/"
    IMAGE_EXTENSION = ".png"

    def __init__(self):
        self.spaces = [
            [None, None, None, None, None, None, None, None],
            [Pawn((0, 1), "black"), Pawn((1, 1), "black"), Pawn((2, 1), "black"), Pawn((3, 1), "black"), Pawn((4, 1), "black"), Pawn((5, 1), "black"), Pawn((6, 1), "black"), Pawn((7, 1), "black")],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ]

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
                square = Rectangle(Point(column * self.SQUARE_SIZE, row * self.SQUARE_SIZE), Point(column * self.SQUARE_SIZE - self.SQUARE_SIZE, row * self.SQUARE_SIZE - self.SQUARE_SIZE))
                if pow(-1, row + column) == 1:
                    square.setFill("#CDC8B1") # White squares
                else:
                    square.setFill("#556B2F") # Black squares
                drawn_spaces[row][column] = square
        for row in range(len(self.spaces)):
            for column in range(len(self.spaces[row])):
                piece = self.spaces[row][column]
                if piece is not None:
                    square_center = drawn_spaces[row][column].getCenter()
                    drawn_pieces[row][column] = Image(square_center, self.PIECE_IMAGES + str(piece) + self.IMAGE_EXTENSION)
        return drawn_spaces, drawn_pieces


def main():
    win = GraphWin("game", 1080, 1080)
    # c = Circle(Point(self.SQUARE_SIZE, self.SQUARE_SIZE), 10)
    # c.draw(win)
    board = Board()
    spaces, pieces = board.draw_board()
    print(spaces)
    print(pieces)
    for row in range(len(spaces)):
        for space in range(len(spaces[row])):
            spaces[row][space].draw(win)
    for row in range(len(pieces)):
        for space in range(len(pieces[row])):
            if pieces[row][space] is not None:
                pieces[row][space].draw(win)
    win.getMouse()  # Pause to view result
    win.close()  # Close window when done



main()
