# Polygon Area Calculator

This is a Python project that includes two classes: `Rectangle` and `Square`. These classes are used to perform various geometric calculations like area, perimeter, and diagonal length. The project also allows for visual representation of the shapes using ASCII art and compares the sizes of different shapes by determining how many times one shape can fit inside another.

## Classes

### Rectangle

- **Attributes:**
  - `width`: The width of the rectangle.
  - `height`: The height of the rectangle.
  
- **Methods:**
  - `set_width(width)`: Sets the width of the rectangle.
  - `set_height(height)`: Sets the height of the rectangle.
  - `get_area()`: Returns the area of the rectangle.
  - `get_perimeter()`: Returns the perimeter of the rectangle.
  - `get_diagonal()`: Returns the diagonal length of the rectangle.
  - `get_picture()`: Returns a string representing the shape using "*". If the width or height is greater than 50, returns "Too big for picture."
  - `get_amount_inside(shape)`: Returns the number of times the given shape can fit inside the rectangle.

### Square (Inherits from Rectangle)

- **Attributes:**
  - `side`: The side length of the square.
  
- **Methods:**
  - `set_side(side)`: Sets the side length of the square and adjusts both the width and height accordingly.
  - `set_width(width)`: Overrides the parent method to ensure the square remains a square.
  - `set_height(height)`: Overrides the parent method to ensure the square remains a square.

## Testing

Unit tests are provided in the `test_polygon_area_calculator.py` file to validate the functionality of the classes. The tests cover all methods in both the `Rectangle` and `Square` classes.

To run the tests, execute the following command in the terminal:

```bash
python -m unittest test_polygon_area_calculator.py
