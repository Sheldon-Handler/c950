import distutils.core
import os
import distutils.extension


def find_packages(directory: str) -> list:
    """
    Finds all packages in the given directory.

    Args:
        directory (str): The directory to search for packages.

    Returns:
        list: A list of packages found in the given directory.
    """

    packages = []
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        # If the directory contains an __init__.py file, it is a package
        if "__init__.py" in files:
            # Get the relative path of the package from the directory
            package = os.path.relpath(root, directory).replace(os.path.sep, ".")
            # Add the package to the list of packages
            packages.append(package)
    return packages


distutils.core.setup(
    name="c950",
    version="1.0.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    scripts=["scripts/create_database.py"],
    test_dir={"": "tests"},
    data_files=[("identifier.sqlite", ["data/identifier.sqlite"])],
    url="",
    license="MIT",
    author="Sheldon Handler",
    author_email="57599804+Sheldon-Handler@users.noreply.github.com",
    description="Data Structures and Algorithms II",
)
