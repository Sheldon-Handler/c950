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

import package


# def cmd_input() -> (int, int):
#     """
#     Get the command line input from the user. The user is prompted to enter an hour and a minute. The function checks
#     that the input is a number between 0 and 23 for the hour and between 0 and 59 for the minute. If the input is not
#     valid, the function raises a ValueError. If the input is valid, the function returns the hour and minute as
#     integers. The function is used to get the time that the user wants to look back into.
#
#
#     Returns:
#         (int, int): The hour and minute as integers.
#
#     Notes:
#         time complexity:
#             best case: O(1)
#             worst case: O(1)
#             average case: O(1)
#         space complexity:
#             best case: O(1)
#             worst case: O(1)
#             average case: O(1)
#     """
#
#     hour = input("Enter hour: ")
#     # Check if the hour is a number between 0 and 23
#     if hour.isdigit() and int(hour) < 24 and int(hour) >= 0:
#         hour = int(hour)
#         minute = input("Enter minute: ")
#         # Check if the minute is a number between 0 and 59
#         if minute.isdigit() and int(minute) < 60 and int(minute) >= 0:
#             minute = int(minute)
#             return hour, minute
#         else:
#             raise ValueError("Invalid input. Please enter a number between 0 and 59.")
#     else:
#         raise ValueError("Invalid input. Please enter a number between 0 and 23.")


def prompt_menu() -> str:
    """
    Get the command line input from the user. The user is prompted to enter a command. The function checks that the input
    is a number between 1 and 3. If the input is not valid, the function raises a ValueError. If the input is valid, the
    function returns the command as a string. The function is used to get the command that the user wants to execute.


    Returns:
        str: The command as a string.

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
    print("Enter number to select an option:\n")
    print("\t 1. Show All Packages")
    print("\t 2. Show Specific Package")
    print("\t 3. Quit")

    options = {1, 2, 3}
    option = None

    while option is None:
        option = input("Enter option number: ")
        if option.isdigit() and int(option) in options:
            option = int(option)
        else:
            print("Invalid option. Please enter a number between 1 and 3.")
            option = None

    command = input("Enter command: ")
    # Check if the command is a number between 1 and 3
    if command.isdigit() and int(command) < 4 and int(command) > 0:
        return command
    else:
        raise ValueError("Invalid input. Please enter a number between 1 and 3.")


def prompt_time() -> datetime.time:
    """
    Get the command line input from the user. The user is prompted to enter an hour, minute, and AM/PM. The function
    checks the input is a number between 1 and 12 for the hour, between 0 and 59 for the minute, and either AM or PM for
    the time of day. If the input is not valid, the function raises a ValueError. If the input is valid, the function
    returns the time as a datetime.time object. The function is used to get the time that the user wants to look back
    into.

    Returns:
        datetime.time: The time as a datetime.time object.
    """
    time_input = None

    while time_input is None:
        time_input = input("Enter time (HH:MM AM/PM): ")
        try:
            time_input = datetime.datetime.strptime(time_input, "%I:%M %p").time()
        except ValueError:
            print("Invalid input. Please enter time in the format HH:MM AM/PM.")
            time_input = None

    return time_input


def show_all_packages(packages: [package.Package], time: datetime.time) -> None:
    """
    Show all the packages in the system. The function prints the ID, address ID, deadline, weight, status, and notes of
    each package in the system. The function is used to display all the packages in the system to the user.


    Returns:
        None

    Notes:
        time complexity:
            best case: O(n)
            worst case: O(n)
            average case: O(n)
        space complexity:
            best case: O(n)
            worst case: O(n)
            average case: O(n)
    """
    print(f"\nAll Packages at {time.strftime('%I:%M %p')}:")

    for package in packages:
        if package.modified_time.resolution < time.resolution:
            old_address = package.modified_time.old_address
            print(
                f"ID: {package.id}, Address: {old_address}, City: {package.delivery_deadline}, State: {package.state}, Zip: {package.zip}, Weight: {package.weight_kilo}, Delivery Status: {package.delivery_status}")
        else:
            print(
                f"ID: {package.id}, Address: {package.address}, City: {package.delivery_deadline}, State: {package.state}, Zip: {package.zip}, Weight: {package.weight_kilo}, Delivery Status: {package.delivery_status}")
        print("\n")


def show_specific_package(packages: [package.Package], time: datetime.time, package_id: int) -> None:
    """
    Show a specific package in the system. The function prompts the user to enter a package ID. The function checks if
    the package ID is valid and if the package exists in the system. If the package ID is not valid or the package does
    not exist, the function raises a ValueError. If the package ID is valid and the package exists, the function prints
    the ID, address ID, deadline, weight, status, and notes of the package. The function is used to display a specific
    package in the system to the user.


    Returns:
        None

    Notes:
        time complexity:
            best case: O(n)
            worst case: O(n)
            average case: O(n)
        space complexity:
            best case: O(n)
            worst case: O(n)
            average case: O(n)
    """

    package_id = input("Enter package ID: ")
    # Check if the package ID is a number
    if package_id.isdigit():
        package_id = int(package_id)
        for package in packages:
            if package.id == package_id:
                print(
                    f"ID: {package.id}, Address: {package.address}, City: {package.delivery_deadline}, State: {package.state}, Zip: {package.zip}, Weight: {package.weight_kilo}, Delivery Status: {package.delivery_status}")
                print("\n")
                return
        raise ValueError("Package does not exist.")
    else:
        raise ValueError("Invalid input. Please enter a number.")
