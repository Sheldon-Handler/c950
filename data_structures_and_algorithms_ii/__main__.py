import tkinter

import data_structures_and_algorithms_ii


newShell = data_structures_and_algorithms_ii.shell.Shell()
newShell.parser.parse_args()

csv_file_path = data_structures_and_algorithms_ii.package_csv_file

root = tkinter.Tk()
app = data_structures_and_algorithms_ii.package_gui.CSVTableApp(
    root, data_structures_and_algorithms_ii.package_csv_file
)
root.mainloop()
