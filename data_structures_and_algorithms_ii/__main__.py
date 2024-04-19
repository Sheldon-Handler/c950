import tkinter

import data_structures_and_algorithms_ii


# newShell = data_structures_and_algorithms_ii.shell.Shell()
# newShell.parser.parse_args()
#
# root = tkinter.Tk()
# app = data_structures_and_algorithms_ii.package_gui.CSVTableApp(
#     root, data_structures_and_algorithms_ii.package_csv_file
# )
# root.mainloop()
def main():

    data_structures_and_algorithms_ii.read_csv_file.get_packages(
        data_structures_and_algorithms_ii.package_csv_file
    )

    # newShell = data_structures_and_algorithms_ii.shell.Shell()
    # newShell.parser.parse_args()
    #
    # root = tkinter.Tk()
    # app = data_structures_and_algorithms_ii.package_gui.CSVTableApp(
    #     root, data_structures_and_algorithms_ii.package_csv_file
    # )
    # root.mainloop()
