import DeliveryPackage

hash_table: staticmethod = list.__new__(cls=DeliveryPackage)


newPackage = DeliveryPackage.delivery_package(package_id=0, address="address", deadline=(12, 30), city="Brooklyn",
                                              postal="11210", weight=42.0, status="delivered")
