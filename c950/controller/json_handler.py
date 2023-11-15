import csv
import json
from dataclasses import dataclass, asdict


def csv_to_json(csv_file: str, json_file: str) -> None:
    """
    This function takes a csv file copies the data to a json file.

    Args:
        csv_file (str): The csv file to copy.
        json_file (str): The json file to copy to.

    Returns:
        None
    """

    # Try to convert the csv file to json
    try:
        # Open the csv file in read mode
        with open(csv_file, mode="r", newline="") as csv_file:
            # Create a csv reader object
            reader = csv.DictReader(csv_file)
            # Create a list of dictionaries
            data = list(reader)
            # Open the json file in write mode
            with open(json_file, mode="w", newline="") as json_file:
                # Write the data to the json file
                json.dump(data, json_file, indent=4)
    # If an error occurs
    except Exception as e:
        # Raise the error
        raise e


def dataclasses_to_json(dataclasses: list[dataclass], json_file: str) -> None:
    """Converts a list of dataclasses into a json file.

    Args:
        dataclasses (list): List of dataclasses to save as json.
        json_file (str): Path to json file to save to.

    Returns:
        None
    """

    # Ensure that the "dataclasses" list is not empty.
    assert len(dataclasses) > 0

    # Ensure that the "dataclasses" list contains only dataclasses
    assert all([dataclass.__class__ == dataclass for dataclass in dataclasses])

    # Variable to save dataclasses as dictionaries
    dataclasses_as_dicts = []

    # Convert dataclasses to dictionaries
    for i in dataclasses:
        # Append the dataclass as a dictionary to the list
        dataclasses_as_dicts.append(i.asdict())

    # Try to write the dataclasses to json
    try:
        # Open the json file in write mode
        with open(json_file, mode="w", newline="") as json_file:
            # Write the data to the json file
            json.dump(dataclasses, json_file, indent=4)
    # If an error occurs
    except Exception as e:
        # Raise the error
        raise e
