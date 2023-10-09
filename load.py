import csv

import setuptools.installer

import hash_table
import package
import configparser

setuptools.installer.fetch_build_egg(dist=setuptools.Distribution, req=setuptools.depends.Require)
class Load:
    def __init__(self):
        with open(file=property.fget("packages_file")) as packages_file:
            csv_reader = csv.DictReader(f=packages_file, dialect=csv.excel)
