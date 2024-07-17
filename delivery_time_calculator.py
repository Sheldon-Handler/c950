#  MIT License
#
#  Copyright (c) 2024 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#  Copyright (c) 2024 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import datetime
import __init__


def delivery_time_calculator(
    distance: float, speed: float = __init__.truck_speed
) -> datetime.time:
    """Calculates the delivery time based on the distance and speed.

    Args:
        distance (float): The distance to be traveled.
        speed (float): The speed of the vehicle.

    Returns:
        datetime.time: The delivery time.

    Notes:
        time complexity:
            best case: O(1)
            worst case: O(1)
            average case: O(1)
        space complexity:
            best case: O(1)
            worst case: O(1)
            average case: O(1)
    """
    time = distance / speed
    hours = int(time)
    minutes = int((time - hours) * 60)
    return datetime.time(hours, minutes)


def time_updater(
    current_time: datetime.time,
    distance: float,
    speed: float = __init__.truck_speed,
) -> datetime.time:
    """Updates the current time based on the delivery time.

    Args:
        current_time (datetime.time): The current time.
        distance (float): The distance to be traveled.
        speed (float): The speed of the vehicle. Defaults to truck_speed.

    Returns:
        datetime.time: The updated time.

    Notes:
        time complexity:
            best case: O(1)
            worst case: O(1)
            average case: O(1)
        space complexity:
            best case: O(1)
            worst case: O(1)
            average case: O(1)
    """
    # Convert the current time to hours
    current_time_converted = current_time.hour + current_time.minute / 60

    # Calculate the delivery time and convert it to hours
    delivery_time = delivery_time_calculator(distance, speed)
    delivery_time_converted = delivery_time.hour + delivery_time.minute / 60

    # Add the current time and delivery time to get the updated time
    updated_time = current_time_converted + delivery_time_converted

    # Convert the updated time to hours and minutes
    hours = int(updated_time)
    minutes = int((updated_time - hours) * 60)

    return datetime.time(hours, minutes)
