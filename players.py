import random

import pingpong


class Player:
    """Player class. Players has a paddle object attribute which can be moved by players."""

    def __init__(self, coordinates, movement_speed=60):
        self.score = 0
        self.reaction_range = 0
        self.paddle = pingpong.Paddle(coordinates=coordinates)
        self.movement_speed = movement_speed

    def move_up(self):
        """Method moves up the player's paddle"""
        self.paddle.sety(self.paddle.ycor() + self.movement_speed)

    def move_down(self):
        """Method moves down the player's paddle"""
        self.paddle.sety(self.paddle.ycor() - self.movement_speed)


class ComputerPlayer(Player):
    """Computer player class"""

    def __init__(self, coordinates):
        """
        reaction_range variable has two number in pixel unit.
        They are used in computer_move() method to generate random number from this range.
        """
        super().__init__(coordinates)
        self.reaction_range = (30, 100)  # Two number should be greater than 30 (Recommendation).

    def computer_move(self, ball):
        """
        This method is a 'brain' of computer in this game.
        Take an example for clarify reaction_range = (60, 100). In each frame of an animation,
        program generate random number from (60, 100) range (let's say 'x').
        If ball is 'x' pixels ahead or below of the paddle center,
        call a proper method (move_up() or move_down()).
        The goal is ball 'y' and paddle 'y' coordinates are equal.
        """
        min_reaction, max_reaction = self.reaction_range
        if self.paddle.ycor() > ball.ycor() + random.uniform(min_reaction, max_reaction):
            self.move_down()
        elif self.paddle.ycor() < ball.ycor() - random.uniform(min_reaction, max_reaction):
            self.move_up()
