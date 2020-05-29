import turtle
import random


class Paddle(turtle.Turtle):

    def __init__(self, coordinates, movement_speed=60):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(coordinates)
        self.movement_speed = movement_speed

    def move_up(self):
        self.sety(self.ycor() + self.movement_speed)

    def move_down(self):
        self.sety(self.ycor() - self.movement_speed)


class Ball(turtle.Turtle):

    speed_parametr = 0.00002
    initial_speed = 0.1

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
