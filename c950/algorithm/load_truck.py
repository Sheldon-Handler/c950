from c950.model.package import Package
from c950.defaults import distances, truck_capacity, truck_speed, number_of_trucks, visited_location_indices, \
    starting_location


def load_truck(truck_id: int, packages: list[Package], distances: list[list[float]] = distances,
               starting_location: int = starting_location, truck_capacity: int = 16):
    """
    Loads packages onto trucks for delivery.

    Returns:
        list: A list of Truck objects, each containing a list of packages to be delivered.
    """

    for package in packages:
        if package.delivery_status == "At Hub" and package.truck_id == truck_id \
                and package.special_notes_attribute_key != "Wrong address listed"\
                and package.special_notes_attribute_key :
            package.delivery_status = "En Route"
            package.truck_id = truck_id
            package.delivery_time = "8:00 AM"
            visited_location_indices.append(package.id)
            print(f"Package {package.id} loaded onto Truck {truck_id} at {package.delivery_time}.")

def load_package(package: Package, truck_id: int, distances: list[list[float]] = distances,
                 starting_location: int = starting_location, truck_capacity: int = truck_capacity):
    """
    Loads a package onto a truck for delivery.

    Returns:
        list: A list of Truck objects, each containing a list of packages to be delivered.
    """

    if package.special_notes_attribute_key == "Can only be on truck" and package.special_notes_attribute_value != truck_id:
        print(f"Package {package.id} cannot be loaded onto Truck {truck_id} at {package.delivery_time}.")
        return
    elif package.special_notes_attribute_key == "Delayed on flight---will not arrive to depot until":



    if package.delivery_status == "At Hub" and package.truck_id == truck_id \
            and package.special_notes_attribute_key != "Wrong address listed":
        package.delivery_status = "En Route"
        package.truck_id = truck_id
        visited_location_indices.append(package.id)
        print(f"Package {package.id} loaded onto Truck {truck_id} at {package.delivery_time}.")
