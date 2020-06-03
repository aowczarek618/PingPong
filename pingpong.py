import random
import turtle


class Paddle(turtle.Turtle):
    """Paddle class: making a paddle object on the screen at given coordinates"""

    def __init__(self, coordinates, strech_wid=5):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=strech_wid, stretch_len=1)
        self.penup()
        self.goto(coordinates)


class Ball(turtle.Turtle):
    """Ball class: making a ball object on the screen with certain speed."""
    speed_parametr = 0.01
    initial_speed = 5

    def __init__(self, coordinates):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.goto(coordinates)

        self.delta_x = random.uniform(-self.initial_speed, self.initial_speed)
        self.delta_y = random.uniform(-self.initial_speed, self.initial_speed)

    def move(self):
        """Method responsible for moving the ball"""
        self.setx(self.xcor() + self.delta_x)
        self.sety(self.ycor() + self.delta_y)

    def reset(self):
        """Method resets the ball position and speed"""
        self.delta_x = random.uniform(-self.initial_speed, self.initial_speed)
        self.delta_y = random.uniform(-self.initial_speed, self.initial_speed)
        self.goto((0, 0))

    def speed_up(self):
        """Method speeds up the ball"""
        if self.delta_x > 0:
            self.delta_x += self.speed_parametr
        else:
            self.delta_x -= self.speed_parametr

        if self.delta_y > 0:
            self.delta_y += self.speed_parametr
        else:
            self.delta_y -= self.speed_parametr
