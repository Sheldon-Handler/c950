import csv
import json.tool

import package

hash_table = []

class HashTable:

    with open("packages.csv", "w") as stream:
        writer = csv.writer(stream)
        for package.Package in hash_table:
            row = writer.writerow(hash_table)
            writer.writerow(row)