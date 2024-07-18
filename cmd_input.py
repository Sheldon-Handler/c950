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
import hash_table
import package
import search_function


def prompt_menu():
    """
    Get the command line input from the user. The user is prompted to enter a command. The function checks that the
    input is a number between 1 and 3. If the input is not valid, the function raises a ValueError. If the input is
    valid, the function returns the command as a string. The function is used to get the command that the user wants to
    execute.

    Returns:
        None
    """

    print("Enter number to select an option:\n")
    print("\t 1. Show All")
    print("\t 2. Show Specific Package")
    print("\t 3. Quit\n")

    option = None

    while option is None:  # O(1) - while loop
        option = input("Enter option number: ")
        if option.isdigit():
            option = int(option)
            if option == 1:
                time_input = prompt_time()
                packages_at_time = package_list_at_time(time_input, __init__.packages)
                show_all_packages(time_input, packages_at_time)
                show_truck_distances(packages_at_time, time_input, __init__.trucks)
                option = None
            elif option == 2:
                time_input = prompt_time()
                show_specific_package(time_input, __init__.packages)
                option = None
            elif option == 3:
                return
            else:
                print("Invalid option. Please enter a number between 1 and 3.")
                option = None
        else:
            print("Invalid option. Please enter a number between 1 and 3.")
            option = None


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


def package_list_at_time(
        time: datetime.time,
        packages: hash_table.HashTable = __init__.packages,
) -> list:
    """
    Get the list of packages at a specific time. The function gets all the packages in the system at a specific time. The
    function is used to get the list of packages in the system at a specific time.

    Args:
        time (datetime.time): The time to check the status of the packages.
        packages (hash_table.HashTable): The HashTable of packages in the system.

    Returns:
        list: A list of packages in the system at the specific time.

    Notes:
        time complexity:
            best case: O(n^2)
            worst case: O(n^2)
            average case: O(n^2)
        space complexity:
            best case: O(n)
            worst case: O(n)
            average case: O(n)
    """
    packages_table = packages.get_all()  # O(n^2) - function call
    packages_list = [i[1] for i in packages_table]  # O(n) - for loop

    return search_function.package_status_at_time(
        packages_list, time
    )  # O(n^2) - function call


def show_all_packages(
        time: datetime.time,
        packages_at_time: [package.Package],
) -> None:
    """
    Show all the packages in the system. The function prints the ID, address ID, deadline, weight, status, and notes of
    each package in the system. The function is used to display all the packages in the system to the user.

    Args:
        time (datetime.time): The time to check the status of the packages.
        packages_at_time ([package.Package]): The list of packages in the system at the specific


    Returns:
        None

    Notes:
        time complexity:
            best case: O(n^2)
            worst case: O(n^2)
            average case: O(n^2)
        space complexity:
            best case: O(n)
            worst case: O(n)
            average case: O(n)
    """

    print(f"\nAll Packages at {time.strftime('%I:%M %p')}:\n")

    # Print all the packages in the system
    for package in packages_at_time:  # O(n) - for loop
        if package.delivery_status == "Delivered":
            print(
                f"ID: {package.id}, Address: {package.address}, City: {package.city}, State: {package.state}, Zip: {package.zip}, Weight: {package.weight_kilo}, Truck: {package.truck_id}, Delivery Deadline: {package.delivery_deadline}, Delivery Status: {package.delivery_status}, Delivery Time: {package.delivery_time}"
            )
        else:
            print(
                f"ID: {package.id}, Address: {package.address}, City: {package.city}, State: {package.state}, Zip: {package.zip}, Weight: {package.weight_kilo}, Truck: {package.truck_id}, Delivery Deadline: {package.delivery_deadline}, Delivery Status: {package.delivery_status}"
            )

    print()


def show_truck_distances(
        packages_at_time: [package.Package],
        time: datetime.time,
        trucks: list = __init__.trucks,
) -> None:
    """
    Show the distances traveled by each truck in the system. The function prints the ID of the truck and the distance
    traveled by the truck. The function is used to display the distances traveled by each truck in the system to the
    user.

    Args:
        time (datetime.time): The time to check the status of the packages.
        trucks (list): The list of trucks in the system.

    Returns:
        None

    Notes:
        time complexity:
            best case: O(n^2)
            worst case: O(n^2)
            average case: O(n^2)
        space complexity:
            best case: O(n)
            worst case: O(n)
            average case: O(n)
    """
    distance_traveled_list = []
    total_distances = float(0)
    for i in trucks:  # O(n) - for loop
        distance_traveled = search_function.distance_traveled(
            i, packages_at_time, time
        )  # O(n^2) - function call
        print(f"Truck {i.id} mileage: {distance_traveled} miles")
        distance_traveled_list.append(distance_traveled)
        total_distances += distance_traveled

    print(
        f"\nTotal mileage of all trucks at {time.strftime('%I:%M %p')}: {total_distances} miles\n"
    )


def show_specific_package(
        time: datetime.time, packages: hash_table.HashTable = __init__.packages
) -> None:
    """
    Show a specific package in the system. The function prompts the user to enter a package ID. The function checks if
    the package ID is valid and if the package exists in the system. If the package ID is not valid or the package does
    not exist, the function raises a ValueError. If the package ID is valid and the package exists, the function prints
    the ID, address ID, deadline, weight, status, and notes of the package. The function is used to display a specific
    package in the system to the user.

    Args:
        time (datetime.time): The time to check the status of the packages.
        packages (hash_table.HashTable): The HashTable of packages in the system.

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

    package_id_input = None

    while package_id_input is None:
        package_id_input = input("Enter package ID: ")

        try:
            package_id_input = int(package_id_input)
            package = search_function.specific_package_at_time(
                packages, package_id_input, time
            )

            if package is None:
                package_id_input = None
                raise ValueError(
                    "Package does not exist. Please enter a valid package ID that exists."
                )
            else:
                if package.delivery_status == "Delivered":
                    print(
                        f"\nID: {package.id}, Address: {package.address}, City: {package.city}, State: {package.state}, Zip: {package.zip}, Weight: {package.weight_kilo}, Truck: {package.truck_id}, Delivery Deadline: {package.delivery_deadline}, Delivery Status: {package.delivery_status}, Delivery Time: {package.delivery_time}\n"
                    )
                else:
                    print(
                        f"\nID: {package.id}, Address: {package.address}, City: {package.city}, State: {package.state}, Zip: {package.zip}, Weight: {package.weight_kilo}, Truck: {package.truck_id}, Delivery Deadline: {package.delivery_deadline}, Delivery Status: {package.delivery_status}\n"
                    )

        except ValueError:
            print("Invalid input. Please enter package ID as an integer.")
