# Probability Calculator

This project includes a simple probability calculator that simulates drawing balls from a hat and calculates the probability of drawing a certain combination of balls. The `Hat` class represents a hat with various colored balls, and the `experiment` function calculates the probability of drawing a specific combination of balls.

## Classes

### `Hat`

Represents a hat containing balls of different colors.

#### Methods

- `__init__(self, **balls)`: Initializes the hat with the specified number of balls of each color.
- `draw(self, num_balls)`: Draws a specified number of balls randomly from the hat. If the number of balls drawn is greater than or equal to the total number of balls, all balls are returned and the hat is emptied.

## Functions

### `experiment(hat, expected_balls, num_balls_drawn, num_experiments)`

Simulates drawing balls from the hat for a number of experiments and calculates the probability of drawing the specified combination of balls.

#### Parameters

- `hat` (Hat): An instance of the `Hat` class.
- `expected_balls` (dict): A dictionary where keys are ball colors and values are the required number of balls of that color.
- `num_balls_drawn` (int): The number of balls to draw in each experiment.
- `num_experiments` (int): The number of experiments to run.

#### Returns

- The probability of drawing the expected balls in the specified number of draws.

#### Example Usage

```python
from probability_calculator import Hat, experiment

# Create a hat with 5 blue balls, 4 red balls, and 2 green balls
hat = Hat(blue=5, red=4, green=2)

# Calculate the probability of drawing 1 red ball and 2 green balls in 4 draws
probability = experiment(hat=hat,
                         expected_balls={'red': 1, 'green': 2},
                         num_balls_drawn=4,
                         num_experiments=2000)

print(probability)
# Example output: 0.356 (will vary each time)
