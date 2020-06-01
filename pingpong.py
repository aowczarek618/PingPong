import turtle
import random


class Paddle(turtle.Turtle):

    def __init__(self, coordinates, movement_speed=60, strech_wid=5):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=strech_wid, stretch_len=1)
        self.penup()
        self.goto(coordinates)
        self.movement_speed = movement_speed


class Ball(turtle.Turtle):

    speed_parametr = 0.01
    initial_speed = 5

    def __init__(self, coordinates):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.goto(coordinates)

        self.dx = random.uniform(-self.initial_speed, self.initial_speed)
        self.dy = random.uniform(-self.initial_speed, self.initial_speed)

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def reset(self):
        self.dx = random.uniform(-self.initial_speed, self.initial_speed)
        self.dy = random.uniform(-self.initial_speed, self.initial_speed)
        self.goto((0, 0))

    def speed_up(self):
        if self.dx > 0:
            self.dx += self.speed_parametr
        else:
            self.dx -= self.speed_parametr

        if self.dy > 0:
            self.dy += self.speed_parametr
        else:
            self.dy -= self.speed_parametr
