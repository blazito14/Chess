import numpy as np
from numpy.typing import NDArray
from colorama import init as colorama_init
from colorama import just_fix_windows_console, Cursor
from termcolor import colored
import sys


class Square:
    def __init__(self, pos: tuple, color, size):
        self.pos = pos
        self.color = color
        self.size = size

    def print_square(self):
        row, col = self.pos
        print(Cursor.POS(col, row) + colored(' ' * self.size, on_color=self.color), end='')
        print(Cursor.POS(1, 11) + '', end='')

    def print_piece(self, icon, color):
        row, col = self.pos
        printedString = ' ' * (self.size // 2) + icon + ' ' * (self.size // 2)
        print(Cursor.POS(col, row) + colored(printedString, color=color, on_color=self.color), end='')
        print(Cursor.POS(1, 11) + '', end='')


class Piece:
    def __init__(self, piece_char: str, color, square: Square):
        self.code = self.__get_code_from_char(piece_char)
        self.icon = self.__get_icon_from_char(piece_char.lower())
        self.color = color
        self.square = square

    def print_piece(self):
        self.square.print_piece(self.icon, self.color)

    def move_piece(self, square):
        self.square.print_square()
        self.square = square
        self.square.print_piece(self.icon, self.color)

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


def print_outline():
    print('\nZoom until the outline below is a good size, then press ENTER\n')
    print(f"{'-' * 8 * 3}")
    for i in range(8):
        print(f"|{' ' * (8 * 3 - 2)}|")
    print(f"{'-' * 8 * 3}")


def enter_buffer():
    print('\033[?1049h', end='')


def exit_buffer():
    print('\033[?1049l', end='')  # Return to main buffer


def clear_current_line():
    print('\033[2K', end='')  # Clear entire line from current position


class Board:
    def __init__(self, bc1, bc2, pc1, pc2, fen_string):
        self.bc1 = bc1
        self.bc2 = bc2
        self.pc1 = pc1
        self.pc2 = pc2
        self.squares = self.__make_squares(bc1, bc2, 1)
        # self.rankPos, self.filePos = make_position_dict(self.squares)
        self.pieces = self.__make_starting_pieces(fen_string, self.squares, pc1, pc2)
        self.offset = 1

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
                squares[y + 8 * x] = Square((7 - x + offset, new_y + offset), color, file_size)
        return squares

    def __make_starting_pieces(self, fen_string, squares, pc1, pc2):
        pieces = []
        rank = 7
        file = 0

        for char in fen_string:
            if debug:
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
            if debug:
                print(f"current_square: {rank + file}, rank: {rank}, file: {file}")
                print(f"Piece created")
                print(f"")

        return pieces


if __name__ == '__main__':
    global debug, super_debug
    debug = False
    super_debug = False

    if super_debug:
        exit_buffer()
        sys.exit(0)

    user_fen_string = 'rn2kb1r/pp2p1pp/2pp1n2/1B3pq1/3PP3/2N2N1b/PPP2PPP/R1BQR1K1 w kq - 0 1'

    if not debug:
        print_outline()
        input()
        enter_buffer()
    board = Board('on_dark_grey', 'on_light_grey', 'white', 'black', user_fen_string)
    if not debug:
        input(Cursor.POS(1, 1) + 'ENTER to print squares')
        clear_current_line()
        board.print_squares()
        clear_current_line()
        input('ENTER to print pieces')
        board.print_pieces()
        clear_current_line()
        input('ENTER to move piece')
        # board.pieces[21].move_piece(board.squares[8*4+5])
        clear_current_line()
        input('ENTER to leave')
        exit_buffer()
