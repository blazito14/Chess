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
    print('\033[2K\r', end='')  # Clear entire line from current position

def clear_line_above():
    print('\033[A\33[2K\r',end='')

def move_cursor_up():
    print('\033[A')