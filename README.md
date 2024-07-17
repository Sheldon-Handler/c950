MIT License

Copyright (c) 2024 Sheldon Handler

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

This code uses a greedy algorithm to solve the problem of routing a vehicle to the nearest next address.

# Strengths of the algorithm:

- The algorithm is simple and easy to understand. It goes to the nearest next address.
- The algorithm is deterministic. It will always return the same result for the same input.

# Alternative algorithms:

- Dijkstra's algorithm: This algorithm can be used to find the shortest path from the hub to all addresses. It is more
  complex than the greedy algorithm, but it can find the most optimal solution in terms of distance.

- Depth-first search: This algorithm can be used to explore all possible routes from the hub to all addresses. However,
  it can revisit a previous address on the way to another address, which may not be the most efficient route.

# Data structures:

- Class: The Package class stores information about each package, Address class stores information about each address,
  and the Truck class stores information about each truck. This allows for easy access to the data and methods related
  to each package, address, and truck.

- HashTable: A hash table is used to store the each package, with the Package class being the value, and the package ID
  being copied from the Package class to serve the key. This allows for quick access to each package by its ID. The
  packages are divided into 10 buckets, with each bucket representing a different hash value and storing each Package in
  one of the ten sublists of the hash table. This allows for faster retrieval of packages by their ID. The hash table is
  stored in a global variable in the __init__.py module, which allows for easy access to the packages from different
  places and keep the latest update version of the package data in one place for retrieval.

- list: Different lists are used to store the addresses and trucks in global variables in the __init__.py module. This
  allows for easy access to the addresses and trucks from different modules. The lists then store the objects of the
  Address and Truck classes, which allows for easy access to the data and methods related to each address and truck. The
  list data structure is used to in many other places of this program, as the default data structure for storing any
  data that has multiple values. A for loop is used to iterate over the list and access each element.

# Alternative data structures:

- namedtuple: A namedtuple could be used to store the data of each package, address, and truck. This would allow for
  easy access to the data using attribute access, similar to a class, but without the need to define a class. However,
  namedtuples are immutable, so they cannot be modified once created. It would necessitate creating a new namedtuple
  that is has the updated data with any non updated data copied over. This would make the code more complex.
- dict: A dict could be used to store the data of each package, address, and truck. This would allow for finding the
  attributes of item by their key, similar to how an attribute value of a class object can be found, but with different
  syntax. However, it is not as easy to access the data as with a class, requiring the use of more exotic methods to
  access the data, which would make the code more complex.

# Things to do differently:

This code has unfortunately been overengineered, with a seperate deliver, load, and departure functions for classes
Package, Truck, and Address. The Truck class has methods that than call those functions from the Package and Address
classes. This could have been simplified by having a single function that handles updating the data in Package, Truck,
and Address classes. This would make the code more readable, maintainable, concise, easier to understand, and require
less jumping between functions that call other functions in different classes. This happened due to confusion on the
actual requirements of the code, and deadline approach made refactoring impossible. There is an unused module called
"table_app.py" that was meant to be used to display the data in a GUI using tkinter, but it was never implemented due to
time constraints. I would use that if I had more time to work on this project.