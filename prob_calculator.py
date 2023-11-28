import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.drawn_balls = []   # balls removed
        self.contents = [] # each ball
        for ball in self.kwargs:
            for i in range(self.kwargs.get(ball)):
                self.contents.append(ball)
    def __str__(self):
        return str(self.contents)
    def draw(self,num_balls):
        if num_balls == 0:
            return self.drawn_balls
        elif num_balls>=len(self.contents):
            self.drawn_balls = self.contents
            return self.drawn_balls
        for drawed_ball in range(num_balls):
            ran_ball = random.randint(0,len(self.contents)-1)
            self.drawn_balls.append(self.contents[ran_ball])
            self.contents.pop(ran_ball)
        return self.drawn_balls
    def test(self,name):
        return self.kwargs.get(name)

def experiment(hat: object, expected_balls: dict, num_balls_drawn: int, num_experiments: int):
    hat_balls = copy.deepcopy(hat)  # count the amount
    hat_balls = str(hat_balls)
    successes = 0
    estr = {}
    for item in hat.contents:
        estr[item] = hat.contents.count(item)
    test = []
    for exp in  range(num_experiments):
        drawn_hats = Hat(**estr).draw(num_balls_drawn) # hats that got drawn
        checker = []
        test.append(drawn_hats)
        for expected_ball in expected_balls:   # ball gets drawn from the balls drawn
                    # expected balls with value and the drawn balls
            if expected_balls.get(expected_ball) <= drawn_hats.count(expected_ball):
                checker.append(True)
            else:
                checker.append(False)
        if all(i for i in checker) == True:
            successes+=1

    return (successes/num_experiments)

