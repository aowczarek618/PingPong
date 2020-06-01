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

    def computer_move(self, ball):
        pass

    @staticmethod
    def is_human():
        return True


class ComputerPlayer(Player):

    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.reaction_range = (60, 100)  # Easy: 10000, Medium: 1000, Hard: 100

    def computer_move(self, ball):
        x, y = self.reaction_range
        if self.paddle.ycor() > ball.ycor() + random.uniform(x, y):
            self.move_down()
        elif self.paddle.ycor() < ball.ycor() - random.uniform(x, y):
            self.move_up()

    @staticmethod
    def is_human():
        return False
