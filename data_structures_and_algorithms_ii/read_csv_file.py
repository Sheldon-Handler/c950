import csv
import datetime

import data_structures_and_algorithms_ii


def get_addresses(
    file,
) -> (data_structures_and_algorithms_ii.hash_table.HashTable, list):
    """
    This function reads a csv file and returns a list of Location objects.

    Args:
        file (): The file to read from.

    Returns:
        list: A list of Location objects.

    Notes:
        time complexity: O(n^2)
        space complexity: O(n)
    """
    address_table = data_structures_and_algorithms_ii.hash_table.HashTable()
    address_list = []

    csv_file = open(file, mode="r", newline="")
    reader = csv.reader(csv_file)

    # Parse the csv file and create a hash table of Address objects
    for row in reader:  # O(n) - for loop
        address_list.append(data_structures_and_algorithms_ii.address.Address(*row))
        address_table.set(
            row[1], data_structures_and_algorithms_ii.address.Address(*row)
        )  # O(n) - setter

    csv_file.close()

    return address_table, address_list


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
    rows = [row for row in csv_reader]  # O(n) - list comprehension

    # Fill in empty cells with the corresponding cell value
    for row in range(len(rows)):  # O(n) - for loop
        for column in range(len(rows[row])):  # O(n) - for loop
            if column == "":
                rows[row][column] = rows[column][row]

    # Convert the distance matrix to a list of floats
    distance_matrix = [[float]]
    for row in rows:  # O(n) - for loop
        distance_matrix.append([float(cell) for cell in row])  # O(n) - for loop

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
    packages = []

    csv_file = open(file, mode="r", newline="")
    reader = csv.reader(csv_file)

    # Parse the csv file and create a list of Package objects
    for row in reader:  # O(n) - for loop
        packages.append(data_structures_and_algorithms_ii.package.Package(*row))

    csv_file.close()

    return packages


if __name__ == "__main__":
    print(get_distances(data_structures_and_algorithms_ii.distance_csv_file))

    exit(0)
