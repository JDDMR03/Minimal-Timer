import src.ui as ui
import src.logic as logic
import src.constants as constants
import time


def main():
    ui.show_welcome_screen()

    while True:
        label, time_input = ui.get_timer_input()
        total_seconds = logic.parse_time_to_seconds(time_input)

        if total_seconds is not None:
            break

        print(f"{constants.RED}Invalid format! Please use hh:mm:ss (e.g. 00:05:00){constants.RESET}")
        time.sleep(1.5)
        ui.show_welcome_screen()

    current_seconds = total_seconds
    show_colon = True

    try:
        while current_seconds >= 0:
            percent = (current_seconds / total_seconds) if total_seconds > 0 else 0

            if percent > 0.5:
                color = constants.GREEN
            elif percent > 0.2:
                color = constants.YELLOW
            else:
                color = constants.RED

            time_str = logic.get_time_components(current_seconds)
            progress_str = logic.get_progress_bar_string(
                current_seconds,
                total_seconds,
                constants.BAR_WIDTH,
                constants.BAR_FILLED,
                constants.BAR_EMPTY
            )

            ui.render_timer(label, time_str, progress_str, color, show_colon)

            time.sleep(0.5)
            show_colon = not show_colon

            if show_colon:
                current_seconds -= 1

        print(f"\n{constants.BOLD}{constants.CYAN}       ¡TIME IS UP!       {constants.RESET}\n")

    except KeyboardInterrupt:
        print(f"\n{constants.YELLOW}Timer stopped by user.{constants.RESET}")


if __name__ == "__main__":
    main()
