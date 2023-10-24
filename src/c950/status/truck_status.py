"""This module contains the TruckStatus Enum class to represent the status of a
truck."""

#  MIT License
#
#  Copyright (c) 2023 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Import enum
import enum


# Status Enum class
class TruckStatus(enum.Enum):
    """Status Enum class to store status of truck delivery.

    Attributes:
        AT_HUB: Enum constant for truck at hub
        EN_ROUTE: Enum constant for truck en route
        RETURNING: Enum constant for truck returning
        FINISHED: Enum constant for truck finished

    Returns:
        TruckStatus: A TruckStatus Enum class instance.
    """

    # Set enum constant for truck at hub
    AT_HUB = 0
    # Set enum constant for truck en route
    EN_ROUTE = 1
    # Set enum constant for truck returning
    RETURNING = 2
    # Set enum constant for truck finished
    FINISHED = 3
