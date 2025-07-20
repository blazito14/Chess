from colorama import Cursor
from termcolor import colored

class Square:
    def __init__(self, pos: tuple, color, size, piece):
        self.pos = pos
        self.color = color
        self.original_color = color
        self.size = size
        self.piece = piece

    def print_square(self):
        row, col = self.pos
        print(Cursor.POS(col, row) + colored(' ' * self.size, on_color=self.color), end='')
        print(Cursor.POS(1, 12) + '', end='')

    def print_piece(self):
        row, col = self.pos
        if self.piece == None:
            icon = ''; color = 'white'
        else:
            icon = self.piece.icon; color = self.piece.color

        printedString = ' ' * (self.size // 2) + icon + ' ' * (self.size // 2)
        print(Cursor.POS(col, row) + colored(printedString, color=color, on_color=self.color), end='')
        print(Cursor.POS(1, 12) + '', end='')

