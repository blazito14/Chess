from colorama import Cursor
from termcolor import colored

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

