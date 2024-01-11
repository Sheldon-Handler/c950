#  MIT License
#
#  Copyright (c) 2024 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import tkinter
from datetime import datetime


class DebugWindow:
    """
    A window for displaying debug information.

    Args:
        root (tkinter.Tk): The root window.
        debug_label (tkinter.Label): The label for the debug information.
        debug_text (tkinter.Text): The text box for the debug information.
        save_button (tkinter.Button): The button for saving the debug information to a log file.
        close_button (tkinter.Button): The button for closing the debug window.

    Methods:
        update_debug_info: Updates the debug information in the debug_text text box.
        save_to_log: Saves the debug information to a log file.
        close_window: Closes the debug window.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Debug Window")

        self.debug_label = tkinter.Label(root, text="Debug Information:")
        self.debug_label.pack()

        self.debug_text = tkinter.Text(root, height=10, width=40)
        self.debug_text.pack()

        self.save_button = tkinter.Button(
            root, text="Save to Log", command=self.save_to_log
        )
        self.save_button.pack()

        self.close_button = tkinter.Button(
            root, text="Close Debug Window", command=self.close_window
        )
        self.close_button.pack()

    def update_debug_info(self, debug_info):
        """
        Updates the debug information in the debug_text text box.

        Args:
            debug_info: The debug information to display.
        """
        self.debug_text.insert(tkinter.END, debug_info)

    def save_to_log(self):
        """
        Saves the debug information to a log file.
        """
        debug_info = self.debug_text.get(1.0, tkinter.END)
        log_file = f"../logs/debug_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

        with open(log_file, "w") as log_file:
            log_file.write(debug_info)

        print(f"Debug information saved to {log_file}")

    def close_window(self):
        """
        Closes the debug window.
        """
        self.root.destroy()


# Example usage:
if __name__ == "__main__":
    root = tkinter.Tk()

    debug_window = DebugWindow(root)

    # Simulate some debug information
    debug_info = "Debug Info Line 1\nDebug Info Line 2"
    debug_window.update_debug_info(debug_info)

    root.mainloop()
