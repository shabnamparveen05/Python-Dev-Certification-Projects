# Arithmetic Formatter

This project is part of the [Scientific Computing with Python certification](https://freecodecamp.org/certification/fcc09c77169-264e-4f13-913e-e87982783eb8/scientific-computing-with-python-v7) from freeCodeCamp.

## Project Overview

The Arithmetic Formatter arranges arithmetic problems vertically and optionally provides the answers. It supports addition and subtraction operations.

## Features

- Handles up to five arithmetic problems at a time.
- Supports both addition and subtraction.
- Validates the input to ensure it adheres to the requirements.
- Optionally displays the results of the operations.

## Usage

To use the arithmetic formatter, import the `arithmetic_formatter.py` file and call the `arithmetic_arranger` function:

```python
from arithmetic_formatter import arithmetic_arranger

print(arithmetic_arranger(['32 + 698', '3801 - 2', '45 + 43', '123 + 49'], True))
