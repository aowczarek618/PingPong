import pingpong
import random


class Player:

    def __init__(self, coordinates):
        self.score = 0
        self.reaction_range = 0
        self.paddle = pingpong.Paddle(coordinates=coordinates)

    def move_up(self):
        self.paddle.sety(self.paddle.ycor() + self.paddle.movement_speed)

    def move_down(self):
        self.paddle.sety(self.paddle.ycor() - self.paddle.movement_speed)


class HumanPlayer(Player):

    def __init__(self, coordinates):
        super().__init__(coordinates)


class ComputerPlayer(Player):

    def __init__(self, coordinates):
        super().__init__(coordinates)

        '''
        reaction_range variable has two number in pixel unit.
        They are used in computer_move() method to generate random number from this range.  
        '''
        self.reaction_range = (60, 100)  # These two values are in pixel unit. Their meaning is if ball is

    '''
    This method is a 'brain' of computer in this game. 
    Take an example for clarify reaction_range = (60, 100). In each frame of an animation, program generate
    random number from (60, 100) range (let's say 'x'). If ball is 'x' pixels ahead or below of the paddle center, call
    a proper method (move_up() or move_down()). The goal is ball 'y' and paddle 'y' coordinates are equal. 
    '''
    def computer_move(self, ball):
        x, y = self.reaction_range
        if self.paddle.ycor() > ball.ycor() + random.uniform(x, y):
            self.move_down()
        elif self.paddle.ycor() < ball.ycor() - random.uniform(x, y):
            self.move_up()
