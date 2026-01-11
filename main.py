import src.constants as constants
import src.logic as logic


def main():
    print(f"{constants.RED}{logic.parse_time_to_seconds("01:30:45")}{constants.RESET}")
    print(f"{constants.GREEN}{logic.get_time_components(5445)}{constants.RESET}")


if __name__ == "__main__":
    main()
