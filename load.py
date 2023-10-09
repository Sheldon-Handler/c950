import csv

class Load:
    def __init__(self):
        with open(file=property.fget("packages_file")) as packages_file:
            csv_reader = csv.DictReader(f=packages_file, dialect=csv.excel)
            for row in csv_reader:
                package_id = row["ID"]
                address = str(row[Address])

                person = Person(name, age)
                people.append(person)