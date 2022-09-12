import copy
import random


# Consider using the modules imported above.


class Hat:
    def __init__(self, **balls):
        self.contents = []
        for k, v in balls.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, number_of_balls):
        balls_removed = []
        number_of_balls = min(number_of_balls, len(self.contents))
        for i in range(number_of_balls):
            balls_removed.append(self.contents.pop(random.randrange(len(self.contents))))
        return balls_removed


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        drawn_ball = copy_hat.draw(num_balls_drawn)
        balls = sum([1 for k, v in expected_balls.items() if drawn_ball.count(k) >= v])
        count += 1 if balls == len(expected_balls) else 0
    probability = count / num_experiments
    return probability