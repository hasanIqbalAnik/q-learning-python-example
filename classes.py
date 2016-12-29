class Circle:
    '''
    There is no Circle object in Pygame. This class would offset that.
    It's much easier to work with it than specifying the x and y coordinates everytiime
    :var circleX
    :var circleY
    '''

    def __init__(self, circleX, circleY):
        self.circleX = circleX
        self.circleY = circleY


class State:
    '''
    this class would hold the game snapshot, used by the
    q learner to index it's table, as well as reward function
    to determine the reward of that particular state.

    :var rectPosition
    :var circlePosition
    '''

    def __init__(self, rect, circle):
        self.rect = rect
        self.circle = circle


