from colorama import init as colorama_init
from colorama import just_fix_windows_console, Cursor
from termcolor import colored
import sys


class Space:
    def __init__(self, pos: tuple, color, size: int):
        self.pos = pos
        self.color = color
        self.size = size

    def print_space(self):
        row, col = self.pos
        print(Cursor.POS(col, row) + colored(' ' * self.size, on_color=self.color), end='')
        print(Cursor.POS(1, 11) + '', end='')

    def print_piece(self, icon, color):
        row, col = self.pos
        printedString = ' ' * (self.size // 2) + icon + ' ' * (self.size // 2)
        print(Cursor.POS(col, row) + colored(printedString, color=color, on_color=self.color), end='')
        print(Cursor.POS(1, 11) + '', end='')


class Piece:
    def __init__(self, name: str, player: int, color, space: Space):
        possible_names = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']
        if name.lower() in possible_names:
            self.name = name.lower()
        else:
            print(f"ERROR: {name} is not a valid piece name")
            sys.exit(1)

        self.player = player
        self.icon = get_piece_icon(self.name)
        self.space = space
        self.color = color

    def print_piece(self):
        self.space.print_piece(self.icon, self.color)

    def move_piece(self, space):
        self.space.print_space()
        self.space = space
        self.space.print_piece(self.icon, self.color)


def get_piece_icon(name: str) -> str:
    pieces = {'pawn': '\u265F',
              'rook': '\u265C',
              'knight': '\u265E',
              'bishop': '\u265D',
              'queen': '\u265B',
              'king': '\u265A'}

    icon = pieces[name]
    return icon


class Board:
    def __init__(self, bc1, bc2, pc1, pc2):
        self.bc1 = bc1
        self.bc2 = bc2
        self.spaces = make_spaces(bc1, bc2, 3)
        self.rankPos, self.filePos = make_position_dict(self.spaces)
        self.pieces = make_starting_pieces(self.spaces, pc1, pc2)

    def print_spaces(self):
        for space in self.spaces:
            space.print_space()

    def print_pieces(self):
        for piece in self.pieces:
            piece.print_piece()


def make_spaces(color1, color2, size):
    spaces = []
    colors = [color1, color2]
    for rankPos in range(8):
        for filePos in range(8):
            newFilePos = filePos * size
            color = colors[(filePos + rankPos) % 2]
            spaces.append(Space((rankPos + 1, newFilePos + 1), color, size))
    return spaces


def make_position_dict(spaces):
    ranks = ['8', '7', '6', '5', '4', '3', '2', '1']
    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    rankDict = {}
    fileDict = {}

    for i, rank in enumerate(ranks):
        rankDict[rank] = spaces[i * 8].pos[0] + (spaces[0].size // 2)

    for i, file in enumerate(files):
        fileDict[file] = spaces[i].pos[1] + (spaces[0].size // 2)

    return rankDict, fileDict


def make_starting_pieces(spaces, pc1, pc2):
    pieceOrder = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
    pieces = []
    for i, space in enumerate(spaces):
        if space.pos[0] == 1:
            pieces.append(Piece(pieceOrder[i % 8], 1, pc2, space))
            continue
        if space.pos[0] == 2:
            pieces.append(Piece('pawn', 1, pc2, space))
            continue
        if space.pos[0] == 7:
            pieces.append(Piece('pawn', 0, pc1, space))
            continue
        if space.pos[0] == 8:
            pieces.append(Piece(pieceOrder[i % 8], 0, pc1, space))

    return pieces


def clear_current_line():
    print('\033[2K', end='')  # Clear entire line from current position


if __name__ == '__main__':
    print('\nZoom until the outline below is a good size, then press ENTER\n')
    print(f"{'-' * 8 * 3}")
    for i in range(8):
        print(f"|{' ' * (8 * 3 - 2)}|")
    print(f"{'-' * 8 * 3}")
    nothing = input()
    print('\033[?1049h', end='')
    board = Board('on_light_grey', 'on_dark_grey', 'white', 'black')
    nothing = input(Cursor.POS(1, 1) + 'ENTER to print spaces')
    clear_current_line()
    board.print_spaces()
    clear_current_line()
    nothing = input('ENTER to print pieces')
    board.print_pieces()
    clear_current_line()
    nothing = input('ENTER to move piece')
    board.pieces[21].move_piece(board.spaces[8 * 4 + 5])
    clear_current_line()
    nothing = input('ENTER to leave')
    print('\033[?1049l', end='')  # Return to main buffer
