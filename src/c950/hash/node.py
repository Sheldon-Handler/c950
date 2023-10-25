"""Node class for hash table chain."""

#  MIT License
#
#  Copyright (c) 2023 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# Node class
class Node:
    """This class represents a node in the hash table chain.

    Attributes:
        key: The key of the node.
        value: The value of the node.
        next (Node): The next node in the chain.

    Returns:
        Node: A Node object instance.

    Examples:
        >>> node = Node(1, 2)
        >>> node.key
        1
        >>> node.value
        2
        >>> node.next
        None
    """

    # Constructor
    def __init__(self, key, value):
        """Initializes a new Node object.

        Args:
            self (): The Node object self reference.
            key (): The hash key of the node.
            value (): The value of the node.

        Returns:
            None
        """
        # Setting key attribute
        self.key = key
        # Setting value attribute
        self.value = value
        # Setting next attribute to none
        self.next = None
