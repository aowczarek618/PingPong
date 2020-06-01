import turtle
import os
import random
import time

import players
import pingpong


def show_score(pen, player1, player2):
    pen.clear()
    pen.write(f"Player1: {player1.score} Player2: {player2.score}", align="center", font=("Courier", 24, "normal"))


def paddle_ball_collisions(player, ball):
    if player.paddle.xcor() > 0:
        multiplication_factor = 1
    else:
        multiplication_factor = -1

    if abs(player.paddle.xcor()) - 20 < abs(ball.xcor()) < abs(player.paddle.xcor()) + 20 and player.paddle.ycor() + PADDLE_WIDTH / 2 > ball.ycor() > player.paddle.ycor() - PADDLE_WIDTH / 2:
        os.system("aplay -q bounce.wav&")
        ball.setx((abs(player.paddle.xcor()) - 20) * multiplication_factor)
        ball.dx *= -1


def main():

    wn = turtle.Screen()
    wn.title("Ping Pong by @TokyoEdTech")
    wn.bgcolor("black")
    wn.setup(width=WIDTH, height=HEIGHT)
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
        wn.onkeypress(player1.move_up, 'w')
        wn.onkeypress(player1.move_down, 's')

    if player2.is_human():
        wn.onkeypress(player2.move_up, 'Up')
        wn.onkeypress(player2.move_down, 'Down')

    # Main game
    while True:
        wn.update()

        # Move ball
        ball.move()
        ball.speed_up()

        # Border checking
        if ball.ycor() > HEIGHT / 2 - 10:
            os.system("aplay -q bounce.wav&")
            ball.sety(HEIGHT / 2 - 10)
            ball.dy *= -1

        if ball.ycor() < -HEIGHT / 2 + 10:
            os.system("aplay -q bounce.wav&")
            ball.sety(-HEIGHT / 2 + 10)
            ball.dy *= -1

        if ball.xcor() > WIDTH / 2 - 10:
            ball.reset()
            player1.score += 1
            show_score(pen, player1, player2)

        if ball.xcor() < -WIDTH / 2 + 10:
            ball.reset()
            player2.score += 1
            show_score(pen, player1, player2)

        # Paddle and ball
        if ball.xcor() < 0:
            paddle_ball_collisions(player1, ball)
        else:
            paddle_ball_collisions(player2, ball)

        # Computer movement
        if not player1.is_human():
            player1.computer_move(ball)

        if not player2.is_human():
            player2.computer_move(ball)

        # End Game
        if player1.score == WIN_SCORE or player2.score == WIN_SCORE:
            pen.clear()
            if player1.score == WIN_SCORE:
                pen.write("Player1 is a winner!", align="center", font=("Courier", 24, "normal"))
            else:
                pen.write("Player2 is a winner!", align="center", font=("Courier", 24, "normal"))
            time.sleep(5)
            break

        time.sleep(0.01)


if __name__ == '__main__':
    WIDTH, HEIGHT = (800, 600)
    WIN_SCORE = 11
    BALL_RADIUS = 10
    STRECH_WID = 5
    PADDLE_WIDTH = 24 * STRECH_WID
    main()
