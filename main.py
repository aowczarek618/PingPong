import turtle
import os
import random
import time

import players
import pingpong


def show_score(pen, player1, player2):
    pen.clear()
    pen.write(f"Player1: {player1.score} Player2: {player2.score}", align="center", font=("Courier", 24, "normal"))


def main():
    width, height = (800, 600)
    win_score = 11

    wn = turtle.Screen()
    wn.title("Ping Pong by @TokyoEdTech")
    wn.bgcolor("black")
    wn.setup(width=width, height=height)
    wn.tracer(0)

    player1 = players.HumanPlayer(coordinates=(-350, 0))
    player2 = players.ComputerPlayer(coordinates=(350, 0))

    # Ball
    ball = pingpong.Ball(coordinates=(0, 0))

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    show_score(pen, player1, player2)

    # Keyboard binding
    wn.listen()
    if player1.is_human():
        wn.onkeypress(player1.paddle.move_up, 'w')
        wn.onkeypress(player1.paddle.move_down, 's')

    if player2.is_human():
        wn.onkeypress(player2.paddle.move_up, 'Up')
        wn.onkeypress(player2.paddle.move_down, 'Down')
    # Main game
    while True:
        wn.update()
        # Scoreboard

        # Move ball
        ball.move()
        ball.speed_up()

        # Border checking
        if ball.ycor() > height / 2 - 10:
            os.system("aplay -q bounce.wav&")
            ball.sety(height / 2 - 10)
            ball.dy *= -1

        if ball.ycor() < -height / 2 + 10:
            os.system("aplay -q bounce.wav&")
            ball.sety(-height / 2 + 10)
            ball.dy *= -1

        if ball.xcor() > width / 2 - 10:
            ball.reset()
            player1.score += 1
            show_score(pen, player1, player2)

        if ball.xcor() < -width / 2 + 10:
            ball.reset()
            player2.score += 1
            show_score(pen, player1, player2)

        # Paddle and ball collisions
        if 340 < ball.xcor() < 350 and player2.paddle.ycor() + 60 > ball.ycor() > player2.paddle.ycor() - 60:
            os.system("aplay -q bounce.wav&")
            ball.setx(340)
            ball.dx *= -1

        if -340 > ball.xcor() > -350 and player1.paddle.ycor() + 60 > ball.ycor() > player1.paddle.ycor() - 60:
            os.system("aplay -q bounce.wav&")
            ball.setx(-340)
            ball.dx *= -1
        # Computer movement
        if not player1.is_human():
            x, y = player1.reaction_range
            if player1.paddle.ycor() > ball.ycor() + random.uniform(x, y):
                player1.paddle.move_down()
            elif player1.paddle.ycor() < ball.ycor() - random.uniform(x, y):
                player1.paddle.move_up()

        if not player2.is_human():
            x, y = player2.reaction_range
            if player2.paddle.ycor() > ball.ycor() + random.uniform(x, y):
                player2.paddle.move_down()
            elif player2.paddle.ycor() < ball.ycor() - random.uniform(x, y):
                player2.paddle.move_up()

        # End Game
        if player1.score == win_score or player2.score == win_score:
            pen.clear()
            if player1.score == win_score:
                pen.write("Player1 is a winner!", align="center", font=("Courier", 24, "normal"))
            else:
                pen.write("Player2 is a winner!", align="center", font=("Courier", 24, "normal"))
            time.sleep(5)
            break


if __name__ == '__main__':
    main()
