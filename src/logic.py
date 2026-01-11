def parse_time_to_seconds(time_str):
    """
    Get total seconds from the string hh:mm:ss
    Return None if invalid
    """

    try:
        parts = time_str.split(':')
        if len(parts) != 3:
            return None

        h, m, s = map(int, parts)

        if not (0 <= m < 60 and 0 <= s < 60 and h >= 0):
            return None

        return (h * 3600) + (m * 60) + s

    except ValueError:
        return None


def get_time_components(total_seconds):
    """
    Transform total_seconds to string hh:mm:ss
    """
    hours = total_seconds // 3600
    total_seconds -= (hours * 3600)
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def get_progress_bar_string(current_seconds, total_seconds, width, filled_char, empty_char):
    """
    Calculate and return the progress bar string
    """

    if total_seconds <= 0:
        return empty_char * width

    filled_count = int((current_seconds / total_seconds) * width)
    empty_count = width - filled_count

    return (filled_char * filled_count) + (empty_char * empty_count)
