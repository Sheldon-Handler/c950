from c950.model.package import Package
from c950.defaults import (
    distances,
    truck_capacity,
    truck_speed,
    number_of_trucks,
    visited_location_indices,
    starting_location,
)


def load_truck(
    truck_id: int,
    packages: list[Package],
    distances: list[list[float]] = distances,
    starting_location: int = starting_location,
    truck_capacity: int = 16,
):
    """
    Loads packages onto trucks for delivery.

    Returns:
        list: A list of Truck objects, each containing a list of packages to be delivered.
    """

    for package in packages:
        if (
            package.delivery_status == "At Hub"
            and package.truck_id == truck_id
            and package.special_notes_attribute_key != "Wrong address listed"
            and package.special_notes_attribute_key
        ):
            package.delivery_status = "En Route"
            package.truck_id = truck_id
            package.delivery_time = "8:00 AM"
            visited_location_indices.append(package.id)
            print(
                f"Package {package.id} loaded onto Truck {truck_id} at {package.delivery_time}."
            )


def check_if_package_can_be_loaded(
    package: Package,
    truck_id: int,
    distances: list[list[float]] = distances,
    starting_location: int = starting_location,
    truck_capacity: int = truck_capacity,
) -> bool:
    """
    Checks if a package can be loaded onto a truck.

    Returns:
        list: A list of Truck objects, each containing a list of packages to be delivered.
    """

    if (
        package.special_notes_attribute_key == "Can only be on truck"
        and package.special_notes_attribute_value != truck_id
    ):
        print(
            f"Package {package.id} cannot be loaded onto Truck {truck_id} at {package.delivery_time}."
            f" It can only be loaded onto Truck {package.special_notes_attribute_value}."
        )
        return False
    elif (
        package.special_notes_attribute_key
        == "Delayed on flight---will not arrive to depot until"
    ):
        print(
            f"Package {package.id} cannot be loaded onto Truck {truck_id} at {package.delivery_time}."
            f" It will not arrive to the depot until {package.special_notes_attribute_value}."
        )
        return False
    elif package.special_notes_attribute_key == "Wrong address listed":
        print(
            f"Package {package.id} cannot be loaded onto Truck {truck_id} because the wrong address is assigned."
        )
        return False
    elif package.delivery_status == "Delivered":
        print(
            f"Package {package.id} has already been delivered from Truck {package.truck_id} at {package.delivery_time}."
        )
        return False
    elif package.delivery_status == "En Route":
        print(
            f"Package {package.id} is currently En Route on Truck {package.truck_id}."
        )
        return False
    elif package.delivery_status == "At Hub" and package.truck_id != (truck_id or None):
        print(f"Package {package.id} is already loaded onto Truck {package.truck_id}.")
        return False
    elif (
        package.delivery_status == "At Hub"
        and package.truck_id == truck_id
        and package.special_notes_attribute_key != "Wrong address listed"
    ):
        print(f"Package {package.id} is already loaded onto Truck {truck_id}.")
        return False
    else:
        return True
