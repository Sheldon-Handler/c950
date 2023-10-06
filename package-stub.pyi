from package import Package
from status import Status

class PackageStub:
    package = Package.__init__(self=Package.__class__, address="973 East 29th St",
                               city="Brooklyn", postal="11210", state="NY", weight=12,
                               deadline="12:30 PM", note="", status=Status.EN_ROUTE)
    print(package)
