import numpy as np
from piece.piece import Piece
from square.square import Square

class Board:
    def __init__(self, bc1, bc2, pc1, pc2, fen_string, debug):
        self.bc1 = bc1
        self.bc2 = bc2
        self.pc1 = pc1
        self.pc2 = pc2
        self.debug = debug
        self.offset = 1
        self.squares = self.__make_squares(bc1, bc2, 1)
        # self.rankPos, self.filePos = make_position_dict(self.squares)
        self.pieces = self.__make_starting_pieces(fen_string, self.squares, pc1, pc2)

    def print_squares(self):
        for square in self.squares:
            square.print_square()

    def print_pieces(self):
        for piece in self.pieces:
            piece.print_piece()

    def __make_squares(self, color1, color2, offset):
        file_size = 3
        squares = np.zeros(shape=64, dtype=object)
        colors = [color1, color2]
        for x in range(8):
            for y in range(8):
                new_y = y * file_size
                color = colors[(x + y) % 2]
                squares[y + 8 * x] = Square((7 - x + offset, new_y + offset), color, file_size, None)
        return squares

    def __make_starting_pieces(self, fen_string, squares, pc1, pc2):
        pieces = []
        rank = 7
        file = 0

        for char in fen_string:
            if self.debug:
                print(f"char: {char}")

            if char == ' ':
                break

            if char == '/':
                rank = rank - 1
                file = 0
                continue

            elif char.isdigit():
                file = file + int(char)
                continue

            if char.isupper():
                color = pc1
            else:
                color = pc2
            current_square = squares[rank * 8 + file]
            current_piece = Piece(char, color, current_square)
            pieces.append(current_piece)
            current_square.piece = current_piece
            file = file + 1
            if self.debug:
                print(f"current_square: {rank + file}, rank: {rank}, file: {file}")
                print(f"Piece created")
                print(f"")

        return pieces

    def flip_board(self):
        file_size = 3
        for square in self.squares:
            x, y = square.pos
            square.pos = 7 + self.offset - x, 7 + self.offset - y*3

        self.print_squares()
        self.print_pieces()
