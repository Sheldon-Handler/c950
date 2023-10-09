# Student ID: 007830903
# Name: Sheldon Handler
import main
import package
import hash_table
import status

newPackage = package.Package.__init__(address="9732", city="brook", state="nt", postal="11210", note="s", status=status.Status.NOT_AVAILABLE, deadline="12:30", weight=42)

print(newPackage.__str__())