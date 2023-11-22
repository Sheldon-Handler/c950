from enum import Enum


class SpecialNotesAttribute(Enum):
    """
    An enum class for the special notes attributes.
    """
    CAN_ONLY_BE_ON_TRUCK = "Can only be on truck"
    DELAYED_ON_FLIGHT = "Delayed on flight---will not arrive to depot until"
    WRONG_ADDRESS_LISTED = "Wrong address listed"
    MUST_BE_DELIVERED_WITH = "Must be delivered with"


dict_of_special_notes_attributes = {
    "Can only be on truck ": SpecialNotesAttribute.CAN_ONLY_BE_ON_TRUCK,
    "Delayed on flight---will not arrive to depot until ": SpecialNotesAttribute.DELAYED_ON_FLIGHT,
    "Wrong address listed ": SpecialNotesAttribute.WRONG_ADDRESS_LISTED,
    "Must be delivered with ": SpecialNotesAttribute.MUST_BE_DELIVERED_WITH
}


class SpecialNotes(str):

    def __init__(self, special_notes: str):
        super().__init__(special_notes)
        self.special_notes = special_notes


    def can_only_be_on_truck(self) -> int:
        """
        Finds the truck that the package must be on. Given a truck id.

        Args:
            list_of_packages (list): A list of Package objects.

        Returns:
            int: The id of the truck that the package must be on.
        """

        # Remove the prefix "Can only be on truck" and any trailing whitespace
        special_notes = self.special_notes.removeprefix("Can only be on truck").strip(" ")
        # Return the id of the truck
        return int(special_notes)

    def delayed_on_flight___will_not_arrive_to_depot_until(self) -> str:
        """
        Finds the time that the package will arrive at hub.

        Args:
            list_of_packages (list): A list of Package objects.

        Returns:
            str: The time that the package must be delivered.
        """

        # Remove the prefix "Delayed on flight---will not arrive to depot until" and any leading or trailing whitespace
        special_notes = self.special_notes.removeprefix("Delayed on flight---will not arrive to depot until ").strip()
        # Return the time
        return special_notes.capitalize()

    def wrong_address_listed(self) -> bool:
        return True


    def must_be_delivered_with(self) -> list[int]:
        """
        Finds the packages that must be delivered with the current package. Given a list of package ids that must be
        delivered with the current package.

        Args:
            list_of_packages (list): A list of Package objects.

        Returns:
            list: A list of packages ids that must be delivered with the current package.
        """

        # Remove the prefix "Must be delivered with" and any trailing whitespace
        special_notes = self.special_notes.removeprefix("Must be delivered with").strip(" ")
        # Split the string into a list of ids
        id_string_list = special_notes.split(",")
        # Convert the list of strings to a list of ints
        id_list = [int(id_string) for id_string in id_string_list]
        # Return the list of ids
        return id_list
