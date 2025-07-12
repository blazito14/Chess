import sys
from utils.utils import *
from colorama import Cursor
from board.board import Board

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
        # board.pieces[21].move_piece(board.squares[8*4+5])
        clear_current_line()
        input('ENTER to leave')
        exit_buffer()
