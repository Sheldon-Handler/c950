import copy

import data_structures_and_algorithms_ii


def fill_blank_columns_in_distance_matrix(distance_matrix: [[float]]) -> [[float]]:
    """
    Parses the distance matrix and fills in any blank columns with the corresponding row values.

    Args:
        distance_matrix (list[list]): A list of lists representing the distance matrix.

    Returns:
        list: A list of lists representing the distance matrix with blank columns filled in.
    """

    # Find the number of rows and columns in the distance matrix
    number_of_rows = len(distance_matrix)

    # Find the maximum number of columns in the distance matrix
    max_number_of_columns = 0
    for row in distance_matrix:  # O(n) - for loop
        if len(row) > max_number_of_columns:
            max_number_of_columns = len(row)

    # Create a copy of the distance matrix to modify
    modified_distance_matrix = copy.deepcopy(distance_matrix)

    # Fill in any blank columns with the corresponding row values
    for i in range(number_of_rows):  # O(n) - for loop
        for j in range(max_number_of_columns):  # O(n) - for loop
            if modified_distance_matrix[i][j] is not type(float):
                modified_distance_matrix[i][j] = modified_distance_matrix[j][i]
            elif modified_distance_matrix[j][i] is not type(float):
                modified_distance_matrix[j][i] = modified_distance_matrix[i][j]

    return modified_distance_matrix
