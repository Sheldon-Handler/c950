from datetime import time


def get_time(time_string: str) -> time:
    if time_string == "EOD":
        return time(hour=23, minute=59, second=59)
    else:
        return time.fromisoformat(time_string)
