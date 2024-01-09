"""This module contains the main function for the program."""
import tkinter

import data_structures_and_algorithms_ii.view.shell
import data_structures_and_algorithms_ii.global_variables
import data_structures_and_algorithms_ii.debug
import data_structures_and_algorithms_ii.view.package_viewer

#  MIT License
#
#  Copyright (c) 2023 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

newShell = data_structures_and_algorithms_ii.view.shell.Shell()
newShell.parser.parse_args()

csv_file_path = data_structures_and_algorithms_ii.global_variables.package_csv_file

root = tkinter.Tk()
app = data_structures_and_algorithms_ii.view.package_viewer.CSVTableApp(
    root, csv_file_path
)
root.mainloop()
