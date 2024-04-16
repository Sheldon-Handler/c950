import csv
import datetime

import data_structures_and_algorithms_ii


def get_addresses(
    file, number_of_buckets: int = 10
) -> (list, data_structures_and_algorithms_ii.hash_table.HashTable):
    """
    This function reads a csv file and returns a list of Location objects.

    Args:
        file (): The file to read from.
        number_of_buckets (int): The number of buckets for the hash table. Defaults to 10.

    Returns:
        list: A list of Location objects.
        HashTable: A hash table of Location objects.

    Notes:
        time complexity: O(n^2)
        space complexity: O(n)
    """
    address_list = []
    address_table = data_structures_and_algorithms_ii.hash_table.HashTable(
        number_of_buckets
    )

    csv_file = open(file, mode="r", newline="")
    reader = csv.reader(csv_file)

    # Parse the csv file and create a hash table of Address objects
    for row in reader:  # O(n) - for loop
        address_list.append(data_structures_and_algorithms_ii.address.Address(*row))
        address_table.set(row[1], row[0])  # O(n) - setter

    csv_file.close()

    return address_list, address_table


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

    # Search for empty cells and fill them with the corresponding cell value
    for row in range(len(rows)):  # O(n) - for loop
        for column in range(len(rows)):  # O(n) - for loop
            # If the cell is empty, fill it with the corresponding cell value
            if (
                rows[row][column] is None or rows[row][column] == ""
            ):  # O(1) - if statement
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
                address=row[1],
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
