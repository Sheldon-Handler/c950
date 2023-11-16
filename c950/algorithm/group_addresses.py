

class PackageGroup:
    """
    Represents a group of packages to be delivered together in a multi-truck delivery scenario.


    """

    def __init__(self, address_list, distance_matrix, locations_assigned_previously: list):
        self.address_list = address_list
        self.distance_matrix = distance_matrix
        self.locations_assigned_previously = locations_assigned_previously

    def calculate_route(self):
        """
        Calculates the optimal route for delivering the packages in the group, considering the starting location.

        Returns:
            list: A list representing the route, with each element representing a package location index.
        """

        route = []
        current_location = self.address_list[0]

        for location in self.address_list:
            route.append(location)
            current_location = location

        # Add a return trip to the starting location
        route.append(self.starting_location)

        return route

def nearest_location(current_location, location_list):

    for i in location_list:
