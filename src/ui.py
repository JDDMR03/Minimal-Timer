import os
import shutil
import src.constants as constants


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_terminal_size():
    size = shutil.get_terminal_size()
    return size.columns, size.lines


def show_welcome_screen():
    clear_screen()
    cols, lines = get_terminal_size()

    title = "TERMINAL TIMER SETUP"
    border = "=" * len(title)

    print("\n" * (lines // 3))
    print(f"{constants.CYAN}{constants.BOLD}{border.center(cols)}{constants.RESET}")
    print(f"{constants.CYAN}{constants.BOLD}{title.center(cols)}{constants.RESET}")
    print(f"{constants.CYAN}{constants.BOLD}{border.center(cols)}{constants.RESET}\n")


def get_timer_input():
    cols, _ = get_terminal_size()
    indent = " " * (cols // 4)
    label = input(f"{indent}{constants.YELLOW}1. Enter a label for the timer: {constants.RESET}")
    time_raw = input(f"{indent}{constants.YELLOW}2. Set Time (hh:mm:ss): {constants.RESET}")
    return label, time_raw


def render_timer(label, time_str, progress_str, color, show_colon):
    clear_screen()
    cols, lines = get_terminal_size()

    display_str = time_str if show_colon else time_str.replace(":", " ")

    ascii_rows = ["", "", "", "", ""]
    for char in display_str:
        for i in range(5):
            ascii_rows[i] += constants.ASCII_DIGITS[char][i] + " "

    ascii_width = len(ascii_rows[0])
    progress_bar_full = f"PROGRESS: [{progress_str}]"

    content_height = 11
    top_padding = max(0, (lines - content_height) // 2)

    print("\n" * top_padding)
    print(f"{color}{constants.BOLD}{('=' * 50).center(cols)}{constants.RESET}")
    print(f"{color}{constants.BOLD}{label.upper().center(cols)}")
    print(f"{color}{('=' * 50).center(cols)}{constants.RESET}\n")

    for row in ascii_rows:
        padding = (cols - ascii_width) // 2
        print(f"{color}{' ' * padding}{row}{constants.RESET}")

    print(f"\n\n{progress_bar_full.center(cols)}")
    print(f"\n{color}{('=' * 50).center(cols)}{constants.RESET}")
