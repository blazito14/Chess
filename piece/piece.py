from square.square import Square
from termcolor import colored
import numpy as np
from numpy.typing import NDArray

class Piece:
    def __init__(self, piece_char: str, color, square: Square):
        self.code = self.__get_code_from_char(piece_char)
        self.icon = self.__get_icon_from_char(piece_char.lower())
        self.color = color
        self.square = square

    def print_piece(self):
        self.square.print_piece()

    def move_piece(self, square):
        self.square.print_square()
        self.square.piece = None
        self.square = square
        self.square.piece = self
        self.square.print_piece()

    def __get_icon_from_char(self, char: str) -> str:
        icons = {'p': '\u265F',
                 'r': '\u265C',
                 'n': '\u265E',
                 'b': '\u265D',
                 'q': '\u265B',
                 'k': '\u265A'}
        return icons[char]

    def __get_code_from_char(self, char: str) -> NDArray(shape=(), dtype=np.uint8):
        no_piece = 0;
        king = 1;
        pawn = 2;
        knight = 3;
        bishop = 4
        rook = 5;
        queen = 6;
        white = 8;
        black = 16

        piece_codes = {'k': king, 'p': pawn, 'n': knight, 'b': bishop,
                       'r': rook, 'q': queen}

        code = np.array(0x00000, dtype=np.uint8)
        code = code | piece_codes[char.lower()]

        if char.isupper():
            code = code | white
        else:
            code = code | black
        return code
