distance_matrix = []

def get_distance_matrix(file) -> list[list]:
    """
    This function reads a csv file and returns a list of lists representing a distance matrix.

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
