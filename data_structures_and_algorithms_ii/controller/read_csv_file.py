import csv

import data_structures_and_algorithms_ii


def package(file) -> list:
    """
    This function reads a csv file and returns a list of Location objects.

    Args:
        file (str): The file to read from.

    Returns:
        list: A list of Location objects.

    Notes:
        time complexity: O(n)
        space complexity: O(n)
    """
    packages = []

    csv_file = open(file, mode="r", newline="")
    reader = csv.reader(csv_file)

    for row in reader:  # O(n) - for loop
        packages.append(data_structures_and_algorithms_ii.model.package.Package(*row))

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

    for row in reader:  # O(n) - for loop
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
    list_of_locations = []

    csv_file = open(file, mode="r", newline="")
    reader = csv.reader(csv_file)

    for row in reader:  # O(n) - for loop
        list_of_locations.append(
            data_structures_and_algorithms_ii.model.address.Address(
                int(row[0]), row[1], row[2]
            )
        )

    csv_file.close()

    return list_of_locations


if __name__ == "__main__":
    print(distance(data_structures_and_algorithms_ii.distance_csv_file))

    exit(0)
