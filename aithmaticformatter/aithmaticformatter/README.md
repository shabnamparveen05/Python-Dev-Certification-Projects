# Arithmetic Formatter

This project provides a function to format a list of arithmetic problems. The `arithmetic_arranger` function arranges the problems in a readable format and can optionally display the answers.

## Function

### `arithmetic_arranger(problems, show_answers=False)`

Formats and arranges arithmetic problems. Optionally displays the answers.

#### Parameters

- `problems` (list of str): A list of arithmetic problems as strings (e.g., ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]).
- `show_answers` (bool, optional): If `True`, the function will include the answers in the output. Default is `False`.

#### Returns

- A string representing the arranged arithmetic problems. If `show_answers` is `True`, the answers are included.

#### Example Usage

```python
from arithmetic_formatter import arithmetic_arranger

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems))

# Output:
#   32      3801      45      123
# + 698    -    2    + 43    + 49
# -----    ------    ----    ----
