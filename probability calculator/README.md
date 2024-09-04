# Probability Calculator

This project is a simple implementation of a probability calculator that simulates drawing balls from a hat and calculates the probability of drawing a certain combination of balls.

## Features

- **Hat Class**: Allows creating a hat with various colored balls and supports drawing a specified number of balls.
- **Experiment Function**: Calculates the probability of drawing a specific combination of balls from the hat.

## Classes

### Hat

The `Hat` class represents a hat containing balls of various colors. 

#### Methods

- `__init__(self, **balls)`: Initializes the hat with the given balls.
- `draw(self, num_balls)`: Draws the specified number of balls from the hat.

### experiment(hat, expected_balls, num_balls_drawn, num_experiments)

Simulates the drawing of balls from the hat for a number of experiments and calculates the probability of drawing the specified combination of balls.

#### Parameters

- `hat`: An instance of the `Hat` class.
- `expected_balls`: A dictionary where keys are ball colors and values are the required number of balls of that color.
- `num_balls_drawn`: The number of balls to draw in each experiment.
- `num_experiments`: The number of experiments to run.

#### Returns

- The probability of drawing the expected balls in the specified number of draws.

## Example Usage

```python
from probability_calculator import Hat, experiment

hat = Hat(blue=5, red=4, green=2)
probability = experiment(hat=hat,
                         expected_balls={'red': 1, 'green': 2},
                         num_balls_drawn=4,
                         num_experiments=2000)
print(probability)
``
