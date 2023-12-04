from c950.model.package import Package


class Packages(list):
    """A list of Package objects."""

    def __init__(self) -> None:
        """Initializes a Packages object.

        Args:
            packages (list): A list of Package objects.
        """
        super().__init__()

    def append(self, package: Package) -> None:
        """Adds a package to the list.

        Args:
            package (Package): A Package object.
        """
        super().append(package)

        self.sort(key=lambda package: package.id)

    def get_package_by_id(self, package_id: int) -> Package:
        """Gets a package by its ID.

        Args:
            package_id (int): The ID of the package to get.

        Returns:
            Package: The package with the specified ID.
        """
        for package in self.packages:
            if package.id == package_id:
                return package

        raise ValueError("Package with id {} not found.".format(package_id))

    def get_index_of_package_by_id(self, package_id: int) -> int or None:
        """Gets the index of a package by its ID.

        Args:
            package_id (int): The ID of the package to get.

        Returns:
            int: The index of the package with the specified ID.
        """
        for package in self.packages:
            if package.id == package_id:
                return self.packages.index(package)

        print("Package with id {} not found.".format(package_id))
        return None

    def get_packages_by_status(self, status: str) -> list[Package]:
        """Gets a list of packages by their status.

        Args:
            status (str): The status of the packages to get.

        Returns:
            list: A list of packages with the specified status.
        """
        packages = []

        for package in self.packages:
            if package.status == status:
                packages.append(package)

        return packages

    def get_packages_by_truck_id(self, truck_id: int) -> list[Package]:
        """Gets a list of packages by their truck ID.

        Args:
            truck_id (int): The ID of the truck to get packages for.

        Returns:
            list: A list of packages with the specified truck ID.
        """
        packages = []

        for package in self.packages:
            if package.truck_id == truck_id:
                packages.append(package)

        return packages
