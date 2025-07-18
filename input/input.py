import sys
from utils import exit_buffer, clear_line_above, move_cursor_up
from time import sleep


def parse_input(user_input: str) -> int:
    special_inputs = ['q', 'c', 'f']
    if len(user_input) != 2 and user_input not in special_inputs:
        new_input = input(f"[rank][file] or c clear or q quit: ")
        clear_line_above()
        return parse_input(new_input)

    if user_input == 'q':
        exit_buffer()
        print(f"\nThanks for playing!\n")
        sys.exit(0)

    if user_input == 'c':
        return -1

    if user_input == 'f':
        return 65

    files = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    ranks = [str(num) for num in range(1, 9)]
    file_char = user_input[0]
    rank_char = user_input[1]

    if file_char not in files:
        new_input = input(f"{file_char} invalid file: ")
        clear_line_above()
        return parse_input(new_input)

    if rank_char not in ranks:
        new_input = input(f"{rank_char} invalid rank: ")
        clear_line_above()
        return parse_input(new_input)

    file = files[file_char]
    rank = int(rank_char) - 1
    square_index = rank * 8 + file
    return square_index


def get_move() -> tuple[int, int]:
    flip_board = 65
    user_string = input("Enter Starting Square: ")
    clear_line_above()
    starting_square = parse_input(user_string)
    if starting_square == -1:
        print(f"Cleared - ", end='')
        return get_move()
    if starting_square == flip_board:
        return flip_board, flip_board

    user_string = input("Enter Ending Square: ")
    clear_line_above()
    ending_square = parse_input(user_string)
    if ending_square == -1:
        print(f"Cleared - ", end='')
        return get_move()

    if starting_square == ending_square:
        print(f"Same square - ", end='')
        return get_move()

    if ending_square == flip_board:
        return flip_board, flip_board

    return starting_square, ending_square


if __name__ == "__main__":
    starting_square, ending_square = get_move()
    print(f"starting_square: {starting_square}, ending_square: {ending_square}")
