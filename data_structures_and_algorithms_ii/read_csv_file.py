import csv
import datetime

import address
import data_structures_and_algorithms_ii.__init__
import data_structures_and_algorithms_ii.address
import data_structures_and_algorithms_ii.hash_table
import data_structures_and_algorithms_ii.package


def init():
    """
    Initializes the data structures and variables for the program.

    Returns:
        None

    Notes:
        time complexity: O(1)
        space complexity: O(1)
    """

    address.addresses = get_addresses(
        data_structures_and_algorithms_ii.address_csv_file
    )
    data_structures_and_algorithms_ii.distances = get_distances(
        data_structures_and_algorithms_ii.distance_csv_file
    )
    data_structures_and_algorithms_ii.packages = get_packages(
        data_structures_and_algorithms_ii.package_csv_file
    )


def get_addresses(
    file,
) -> (list, data_structures_and_algorithms_ii.hash_table.HashTable):
    """
    This function reads a csv file and returns a list of Location objects.

    Args:
        file (): The file to read from.

    Returns:
        list: A list of Address objects.

    Notes:
        time complexity: O(n^2)
        space complexity: O(n)
    """
    address_list = []
    csv_reader = csv.reader(file)
    # Read the csv file and store the rows in a list
    for row in csv_reader:
        address_list.append(
            data_structures_and_algorithms_ii.address.Address(
                id=int(row[0]),
                name=row[1],
                address=row[2],
            )
        )


def get_distances(file) -> [[float]]:
    """
    This function reads a csv file and returns a list of Location objects.

    Args:
        file (): The file to read from.

    Returns:
        list[list]: List of distance data from csv file as a distance matrix.

    Notes:
        time complexity: O(n^2)
        space complexity: O(n)
    """
    csv_reader = csv.reader(file)
    # Read the csv file and store the rows in a list
    rows = [row for row in csv_reader]  # O(n) - list comprehension

    # Convert the distance matrix to a list of floats
    distance_matrix = [[float]]

    for row in rows:  # O(n) - for loop
        distance_matrix.append([float(cell) for cell in row])  # O(n) - for loop

    # Search for empty cells and fill them with the corresponding cell value
    for row in range(len(rows)):  # O(n) - for loop
        for column in range(len(rows)):  # O(n) - for loop
            # If the cell is empty, fill it with the corresponding cell value
            if (
                rows[row][column] is None or rows[row][column] == ""
            ):  # O(1) - if statement
                rows[row][column] = rows[column][row]

    return distance_matrix


def get_packages(file) -> list:
    """
    This function reads a csv file and returns a list of Package objects.

    Args:
        file (str): The file to read from.

    Returns:
        list: A list of Package objects.

    Notes:
        time complexity: O(n)
        space complexity: O(n)
    """

    # Create an empty list to store the packages
    packages = []

    csv_file = open(file, mode="r", newline="")
    reader = csv.reader(csv_file)

    # Parse the csv file and create a list of Package objects
    for row in reader:  # O(n) - for loop

        # Create a Package object and add it to the list
        packages.append(
            data_structures_and_algorithms_ii.package.Package(
                id=int(row[0]),
                address=data_structures_and_algorithms_ii.address.get_address(
                    row[1]
                ),  # O(n) - function call
                city=row[2],
                state=row[3],
                zip=row[4],
                delivery_deadline=(
                    datetime.time(hour=23, minute=59)
                    if row[5] == "EOD"
                    else datetime.datetime.strptime(row[5], "%I:%M %p").time()
                ),
                weight_kilo=int(row[6]),
                special_notes=row[7],
            )
        )

    csv_file.close()

    return packages


if __name__ == "__main__":
    print(get_distances(data_structures_and_algorithms_ii.distance_csv_file))

    exit(0)
