from colorama import init as colorama_init
from colorama import just_fix_windows_console
from termcolor import colored

colorama_init()
just_fix_windows_console()

all_colors = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'light_grey', 'dark_grey',
              'light_red', 'light_green', 'light_yellow', 'light_blue', 'light_magenta', 'light_cyan']
all_styles = ['classic', 'simple', 'fancy', 'scribble']

c_1 = 'blue'
c_2 = 'black'
bc_1 = (234, 236, 209)
bc_2 = (114, 149, 82)


def draw_new_board(c_1, c_2, bc_1, bc_2):
    pieces = {'pawn': '\u265F',
              'rook': '\u265C',
              'knight': '\u265E',
              'bishop': '\u265D',
              'queen': '\u265B',
              'king': '\u265A'}

    if type(bc_1) is tuple:
        if type(bc_2) is tuple:
            backgrounds = [bc_1, bc_2]
        elif type(bc_2) is str:
            backgrounds = [bc_1, "on_" + bc_2]
        else:
            print(f"Invalid type for background 2. Must be string or tuple")
    elif type(bc_1) is str:
        if type(bc_2) is tuple:
            backgrounds = ["on_" + bc_1, bc_2]
        elif type(bc_2) is str:
            backgrounds = ["on_" + bc_1, "on_" + bc_2]
        else:
            print(f"Invalid type for background 2. Must be string or tuple")
    else:
        print(f"Invalid type for background 1. Must be string or tuple")

    board = {'ranks': ['8', '7', '6', '5', '4', '3', '2', '1'],
             'files': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']}

    for rank in board['ranks']:
        for rank_num, file in enumerate(board['files']):
            background = backgrounds[(rank_num + int(rank)) % 2]

            if rank == '1' or rank == '2':
                color = c_1
            elif rank == '7' or rank == '8':
                color = c_2
            if 2 < int(rank) and int(rank) < 7:
                print(colored('   ', on_color=background), end='')
                continue

            elif rank == '2':
                piece = pieces['pawn']

            elif rank == '7':
                piece = pieces['pawn']

            elif rank == '1' or rank == '8':
                if file == 'a' or file == 'h':
                    piece = pieces['rook']
                elif file == 'b' or file == 'g':
                    piece = pieces['knight']
                elif file == 'c' or file == 'f':
                    piece = pieces['bishop']
                elif file == 'd':
                    piece = pieces['queen']
                elif file == 'e':
                    piece = pieces['king']

            print(colored(' ' + piece + ' ', color, background), end='')
        print('')

    '''
    for color in pieces.keys():
        for idx, piece in enumerate(pieces[color].keys()):
            real_idx = idx
            if color == 'black':
                real_idx = idx + 1
            background = backgrounds[real_idx % 2]
            print(colored(' ', color, background), end='')
            print(colored(pieces[color][piece], color, background),end='')
            print(colored(' ', color, background), end='')
    
        print('')
    '''


if __name__ == '__main__':
    draw_new_board(c_1, c_2, bc_1, bc_2)
