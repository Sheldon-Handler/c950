from delivery_package import DeliveryPackage
from status import Status

class DeliveryPackageStub:
    DeliveryPackage.__init__(self=DeliveryPackage.__base__, address="973 East 29th St",
                                              city="Brooklyn", zip="11210", state="NY", weight=12,
                                              deadline="12:30 PM", note="", status=Status)
