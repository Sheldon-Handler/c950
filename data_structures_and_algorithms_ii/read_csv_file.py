import csv

import data_structures_and_algorithms_ii


def package(file) -> list:
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
        # Create a Package object and add it to the list of packages
        packages.append(package.Package(*row))

    csv_file.close()

    return packages


def distance(file) -> list[list]:
    """
    This function reads a csv file and returns a list of Location objects.

    Args:
        file (str): The file to read from.

    Returns:
        list[list]: List of distance data from csv file as a distance matrix.

    Notes:
        time complexity: O(n)
        space complexity: O(n)
    """
    rows = []

    csv_file = open(file, mode="r", newline="")
    reader = csv.reader(csv_file)

    # Parse the csv file and create a list of lists representing the distance matrix
    for row in reader:  # O(n) - for loop
        # Add the row to the list of rows
        rows.append(row)

    return rows


def address(file) -> list:
    """
    This function reads a csv file and returns a list of Location objects.

    Args:
        file (): The file to read from.

    Returns:
        list: A list of Location objects.

    Notes:
        time complexity: O(n)
        space complexity: O(n)
    """
    addresses = []

    csv_file = open(file, mode="r", newline="")
    reader = csv.reader(csv_file)

    # Parse the csv file and create a list of Address objects
    for row in reader:  # O(n) - for loop
        # Create an Address object and add it to the list of addresses
        addresses.append(address.Address(int(row[0]), row[1], row[2]))

    csv_file.close()

    return addresses


if __name__ == "__main__":
    print(distance(data_structures_and_algorithms_ii.distance_csv_file))

    exit(0)
