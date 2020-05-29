import turtle

width, height = (800, 600)
wn = turtle.Screen()
wn.title("Ping Pong by @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width=width, height=height)
wn.tracer(0)

# Score variables
score_a = 0
score_b = 0


class Paddle(turtle.Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(coordinates)

    def move_up(self):
        self.sety(self.ycor() + 20)

    def move_down(self):
        self.sety(self.ycor() - 20)


class Ball(turtle.Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(coordinates)

        self.dx = 0.2
        self.dy = -0.2

    def move(self):
        self.setx(ball.xcor() + ball.dx)
        self.sety(ball.ycor() + ball.dy)


# Paddle A
paddle_a = Paddle(coordinates=(-350, 0))

# Paddle B
paddle_b = Paddle(coordinates=(350, 0))

# Ball
ball = Ball(coordinates=(0, 0))

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"PlayerA: {score_a} PlayerB: {score_b}", align="center", font=("Courier", 24, "normal"))

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a.move_up, 'w')
wn.onkeypress(paddle_a.move_down, 's')
wn.onkeypress(paddle_b.move_up, 'Up')
wn.onkeypress(paddle_b.move_down, 'Down')
# Main game loop
while True:
    wn.update()
    # Scoreboard

    # Move ball
    ball.move()

    # Border checking
    if ball.ycor() > height / 2 - 10:
        ball.sety(height / 2 - 10)
        ball.dy *= -1

    if ball.ycor() < -height / 2 + 10:
        ball.sety(-height / 2 + 10)
        ball.dy *= -1

    if ball.xcor() > width / 2 - 10:
        ball.goto((0, 0))
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"PlayerA: {score_a} PlayerB: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -width / 2 + 10:
        ball.goto((0, 0))
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"PlayerA: {score_a} PlayerB: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if 340 < ball.xcor() < 350 and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1

    if -340 > ball.xcor() > -350 and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1
