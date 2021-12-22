from abc import *


class Piece:
    type = ""
    position = (0, 0)
    color = "black"

    def __init__(self, type, pos, color):
        self.type = type
        self.position = pos
        self.color = color

    def __eq__(self, other):
        if str(self) == str(other):
            return True
        else:
            return False

    def __str__(self):
        return self.color + "_" + self.type

    def position_add(self, distance):
        """
        returns a position which is the piece's current position moved by distance
        :param distance: The distance to move the piece in the X and Y directions
        :return:
        """
        return (self.position[0] + distance[0], self.position[1] + distance[1])

    @abstractmethod
    def valid_moves(self):
        pass


class Pawn(Piece):
    moved = False
    direction_scalar = 1

    def __init__(self, pos, color):
        super().__init__("pawn", pos, color)
        if color == "white":
            self.direction_scalar = 1
        elif color == "black":
            self.direction_scalar = -1

    def valid_moves(self):
        move_set = set()
        if not self.moved:
            move_set.add(self.position_add((0, self.direction_scalar * 1)))
            move_set.add(self.position_add((0, self.direction_scalar * 2)))
        else:
            move_set.add()