import os
import src.constants as constants


def clear_screen():
    """
    Clear the screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def show_welcome_screen():
    """
    Just the welcome banner
    """
    print(f"{constants.CYAN}{constants.BOLD}======================================={constants.RESET}")
    print(f"{constants.CYAN}{constants.BOLD}       TERMINAL TIMER SETUP            {constants.RESET}")
    print(f"{constants.CYAN}{constants.BOLD}======================================={constants.RESET}\n")


def get_timer_input():
    """
    Capture the user input
    """
    label = input(f"{constants.YELLOW}1. Enter a label for the timer: {constants.RESET}")
    time_raw = input(f"{constants.YELLOW}2. Set Time (hh:mm:ss): {constants.RESET}")
    return label, time_raw


def render_timer(label, time_str, progress_str, color, show_colon):
    """
    Draws the interfase.
    """
    clear_screen()
    print(f"\n{color}{constants.BOLD}{'=' * 50}")
    print(f"{label.upper()}")
    print(f"{'=' * 50}{constants.RESET}\n")

    # Si show_colon es False, reemplazamos los ':' por espacios vacíos
    display_str = time_str if show_colon else time_str.replace(":", " ")

    # Dibujamos las 5 filas del Arte ASCII
    for row in range(5):
        line = "    "  # Margen izquierdo
        for char in display_str:
            line += constants.ASCII_DIGITS[char][row] + " "
        print(f"{color}{line}{constants.RESET}")

    # Dibujamos la barra de progreso
    print(f"\n\n    PROGRESS: [{color}{progress_str}{constants.RESET}]")
    print(f"\n{color}{'=' * 50}{constants.RESET}")
