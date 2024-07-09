#  MIT License
#
#  Copyright (c) 2024 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


def cmd_input() -> (int, int):
    """
    Get the command line input from the user. The user is prompted to enter an hour and a minute. The function checks
    that the input is a number between 0 and 23 for the hour and between 0 and 59 for the minute. If the input is not
    valid, the function raises a ValueError. If the input is valid, the function returns the hour and minute as
    integers. The function is used to get the time that the user wants to look back into.


    Returns:
        (int, int): The hour and minute as integers.
    """

    hour = input("Enter hour: ")
    # Check if the hour is a number between 0 and 23
    if hour.isdigit() and int(hour) < 24 and int(hour) >= 0:
        hour = int(hour)
        minute = input("Enter minute: ")
        # Check if the minute is a number between 0 and 59
        if minute.isdigit() and int(minute) < 60 and int(minute) >= 0:
            minute = int(minute)
            return hour, minute
        else:
            raise ValueError("Invalid input. Please enter a number between 0 and 59.")
    else:
        raise ValueError("Invalid input. Please enter a number between 0 and 23.")
