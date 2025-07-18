import sys
from utils.utils import *
from colorama import Cursor
from board.board import Board
from input import get_move

if __name__ == '__main__':
    global debug
    if len(sys.argv) >= 2 and sys.argv[1] == '-debug':
        debug = True
    else:
        debug = False

    user_fen_string = 'rn2kb1r/pp2p1pp/2pp1n2/1B3pq1/3PP3/2N2N1b/PPP2PPP/R1BQR1K1 w kq - 0 1'

    if not debug:
        print_outline()
        input()
        enter_buffer()
    board = Board('on_dark_grey', 'on_light_grey', 'white', 'black', user_fen_string, debug)
    if not debug:
        input(Cursor.POS(1, 1) + 'ENTER to print squares')
        clear_current_line()
        board.print_squares()
        clear_current_line()
        input('ENTER to print pieces')
        board.print_pieces()
        clear_current_line()
        input('ENTER to move piece')
        clear_line_above()
        while True:
            starting_square, ending_square = get_move()
            if starting_square == 65 or ending_square == 65:
                board.flip_board()
                continue
            piece = board.squares[starting_square].piece
            if piece == None:
                print(f"no piece - ", end='')
                continue
            piece.move_piece(board.squares[ending_square])

