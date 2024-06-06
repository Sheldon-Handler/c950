import csv
import os

import data_structures_and_algorithms_ii
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

    data_structures_and_algorithms_ii.addresses = get_addresses(
        data_structures_and_algorithms_ii.address_csv_file
    )
    data_structures_and_algorithms_ii.distances = get_distances(
        data_structures_and_algorithms_ii.distance_csv_file
    )
    data_structures_and_algorithms_ii.packages = get_packages(
        data_structures_and_algorithms_ii.package_csv_file
    )


def get_addresses(
    file: os.path.relpath = data_structures_and_algorithms_ii.address_csv_file,
) -> list:
    """
    This function reads a csv file and returns a list of Address objects.

    Args:
       file (): The file to read from.

    Returns:
        list: A list of Address objects.

    Notes:
        time complexity: O(n^2)
        space complexity: O(n)
    """
    addresses = []
    # Open the csv file and read the rows into a list
    csv_file = open(file, "r")
    csv_reader = csv.reader(csv_file)  # O(n) - readlines

    # Read the csv file and store the rows in a list
    for i in csv_reader:  # O(n) - for loop
        addresses.append(
            data_structures_and_algorithms_ii.address.Address(
                id=int(i[0]), name=str(i[1]), address=str(i[2])
            )
        )  # O(1) - function call

    return addresses


def get_distances(
    file: os.path.realpath = data_structures_and_algorithms_ii.distance_csv_file,
) -> [[float]]:
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
    distance_matrix = []
    csv_reader = csv.reader(open(file, "r"))  # O(n) - readlines

    # Read the csv file and store the rows in a list
    for row in csv_reader:  # O(n) - for loop
        distance_row = []
        # Convert the string values to float values
        for column in row:  # O(n) - for loop
            if column == "":
                # If the value is empty, add None to the distance matrix
                distance_row.append(None)
            else:
                # If the value is not empty, convert it to a float and add it to the distance matrix
                distance_row.append(float(column))
        # Add the row to the distance matrix
        distance_matrix.append(distance_row)

    # Fill in the missing values in the distance matrix
    for row in range(len(distance_matrix)):  # O(n) - for loop
        for column in range(len(distance_matrix[row])):  # O(n) - for loop
            if distance_matrix[row][column] is None:
                distance_matrix[row][column] = distance_matrix[column][row]

    return distance_matrix


def get_packages(
    file: os.path.realpath = data_structures_and_algorithms_ii.package_csv_file,
) -> data_structures_and_algorithms_ii.hash_table.HashTable:
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

    # Open the csv file and read the rows into a list
    csv_file = open(file, "r")
    reader = csv.reader(csv_file)  # O(n) - readlines

    # Parse the csv file and create a list of Package objects
    for row in reader:  # O(n) - for loop

        matching_address = None
        for address in data_structures_and_algorithms_ii.addresses:
            if address.address == row[1]:
                matching_address = address
                break

        # Create a Package object and add it to the list
        packages.append(
            data_structures_and_algorithms_ii.package.Package(
                id=int(row[0]),
                address=matching_address,
                city=row[2],
                state=row[3],
                zip=row[4],
                delivery_deadline=(row[5]),
                weight_kilo=int(row[6]),
                special_notes=row[7],
            )
        )

    __hash_table__ = data_structures_and_algorithms_ii.hash_table.HashTable()
    for package in packages:
        __hash_table__.add(package.id, package)

    return __hash_table__


if __name__ == "__main__":
    print(get_distances(data_structures_and_algorithms_ii.distance_csv_file))

    exit(0)
