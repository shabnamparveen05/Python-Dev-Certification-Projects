import random

class Hat:
    def __init__(self, **balls):
        # Create the contents list based on the input arguments
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        # If num_balls is greater than the available balls, return all balls
        if num_balls >= len(self.contents):
            drawn_balls = self.contents[:]
            self.contents.clear()  # Clear the hat since all balls are drawn
            return drawn_balls
        
        # Randomly draw the specified number of balls
        drawn_balls = random.sample(self.contents, num_balls)
        
        # Remove drawn balls from the contents
        for ball in drawn_balls:
            self.contents.remove(ball)
        
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    
    for _ in range(num_experiments):
        # Create a copy of the hat's contents for each experiment
        experiment_hat = Hat(**{color: hat.contents.count(color) for color in set(hat.contents)})
        drawn_balls = experiment_hat.draw(num_balls_drawn)
        
        # Check if the drawn balls meet the expected conditions
        success = True
        for color, count in expected_balls.items():
            if drawn_balls.count(color) < count:
                success = False
                break

        if success:
            success_count += 1

    # Return the probability as the ratio of successful experiments to total experiments
    return success_count / num_experiments

# Example usage to test the code:
hat = Hat(blue=5, red=4, green=2)
probability = experiment(hat=hat,
                         expected_balls={'red': 1, 'green': 2},
                         num_balls_drawn=4,
                         num_experiments=2000)
print(probability)  # Example output: 0.356 (will vary each time)
