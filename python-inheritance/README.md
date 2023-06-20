# Python - Inheritance

## Function Prototypes

Prototypes for functions written in this project:

| File                    | Prototype                             |
| ----------------------- | ------------------------------------- |
| `0-lookup.py`           | `def lookup(obj):`                    |
| `2-is_same_class.py`    | `def is_same_class(obj, a_class):`    |
| `3-is_kind_of_class.py` | `def is_kind_of_class(obj, a_class):` |
| `4-inherits_from.py`    | `def inherits_from(obj, a_class):`    |

## Tasks

* **0. Lookup**
  * Python function that returns a list of available attributes
  and methods of an objects.

* **1. My list**
  * Python class `MyList` that inherits from `list`. Includes:
    * Public instance method `def print_sorted(self):` that prints the list in
    ascending sorted order (assumes all list elements are `int`s).

* **2. Exact same object**
  * Python function that returns `True` if an object is
  exactly an instance of a specified class; otherwise `False`.

* **3. Same class or inherit from**
  * Python function that returns `True` if an object is
  an instance or inherited instance of a specified class; otherwise `False`.

* **4. Only sub class of**
  * Python function that returns `True` if an object is
  an inherited instance (either directly or indirectly) from a specified class;
  otherwise `False`.

* **5. Geometry module**
  * An empty Python class `BaseGeometry`.

* **6. Improve Geometry**
  * Python class `BaseGeometry`. Builds on
  **5-base_geometry.py** with:
    * Public instance method `def area(self):` that raises an `Exception` with
    the message `area() is not implemented`.

* **7. Integer validator**
  * Python class `BaseGeometry`. Builds on
  **6-base_geometry.py** with:
    * Public instance method `def integer_validator(self, name, value):` that
    validates the parameter `value`.
    * Assumes the parameter `name` is always a string.
    * The parameter `value` must be an `int`, otherwise, a `TypeError` exception
    is raised with the message `<name> must be an integer`.
    * The parameter `value` must be greater than `0`, otherwise, a
    `ValueError` exception is raised with the message `<value> must be greater
    than 0`.

* **8. Rectangle**
  * Python class `Rectangle` that inherits from `BaseGeometry`
  **7-base_geometry.py**. Includes:
    * Private attributes `width` and `height` - validated with `integer_validator`.
    * Instantiation with `width` and `height`: `def __init__(self, width, height):`

* **9. Full rectangle**
  * Python class `Rectangle` that inherits from `BaseGeometry`
  **7-base_geometry.py**. Builds on [8-rectangle.py](./8-rectangle.py) with:
    * Implementation of the method `area()`.
    * Special method `__str__` to print `Rectangle`s in the format `[Rectangle]
    <width>/<height>`.

* **10. Square #1**
  * Python class `Square` that inherits from `Rectangle`
  **9-rectangle.py**. Includes:
    * Private attribute `size` - validated with `integer_validator`.
    * Instantiation with `size`: `def __init__(self, size):`.
    * Implementation of the `area()` method.

* **11. Square #2**
  * Python class `Square` that inherits from `Rectangle`
  **9-rectangle.py**. Builds on **10-square.py** with:
    * Special method `__str__` to print squares in the format `[Square]
    <width>/<height>`.



### **Authors**
--- 

![GitHub Contributors Image](https://contrib.rocks/image?repo=RM92023/holbertonschool-low_level_programming)
Robinson Muñetón Jaramillo - <a href="https://github.com/RM92023" target="_blank"> @RM92023</a> ![Your Repository's Stats](https://github-readme-stats.vercel.app/api?username=RM92023&show_icons=true)
