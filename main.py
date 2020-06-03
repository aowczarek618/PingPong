import os
import sys
import time
import turtle

import pingpong
import players


def show_score(pen, player1, player2):
    """Function shows score on the screen."""
    pen.clear()
    pen.write(f"Player1: {player1.score} Player2: {player2.score}", align="center", font=("Courier", 24, "normal"))


def paddle_ball_collisions(player, ball):
    """Function checks paddle and ball collisions."""
    if player.paddle.xcor() > 0:
        multiplication_factor = 1
    else:
        multiplication_factor = -1

    if abs(player.paddle.xcor()) - 20 < abs(ball.xcor()) < abs(player.paddle.xcor()) + 20 and player.paddle.ycor() + PADDLE_WIDTH / 2 > ball.ycor() > player.paddle.ycor() - PADDLE_WIDTH / 2:
        play_sound()
        ball.setx((abs(player.paddle.xcor()) - 20) * multiplication_factor)
        ball.delta_x *= -1


def play_sound():
    """Function plays bounce ball sound."""
    if PLATFORM == "linux":
        os.system("aplay -q bounce.wav&")
    elif PLATFORM == "darwin":
        os.system("afplay -q bounce.wav&")
    elif PLATFORM == "windows":
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


def main():
    """Main function"""
    # Creating a game screen.
    window = turtle.Screen()
    window.title("Ping Pong by @aowczarek618")
    window.bgcolor("black")
    window.setup(width=WIDTH, height=HEIGHT)
    window.tracer(0)

    # Creating players.
    player1 = players.Player(coordinates=(-350, 0))
    player2 = players.ComputerPlayer(coordinates=(350, 0))

    # Creating a ball.
    ball = pingpong.Ball(coordinates=(0, 0))

    # Pen used to write a score on the screen.
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    show_score(pen, player1, player2)

    # Keyboard bindings.
    window.listen()
    if isinstance(player1, players.Player):
        window.onkeypress(player1.move_up, 'w')
        window.onkeypress(player1.move_down, 's')

    if isinstance(player2, players.Player):
        window.onkeypress(player2.move_up, 'Up')
        window.onkeypress(player2.move_down, 'Down')

    # Main game loop.
    while True:
        window.update()

        # Moving and speeding up the ball.
        ball.move()
        ball.speed_up()

        # Checking border collisions.
        if ball.ycor() > HEIGHT / 2 - 10:
            play_sound()
            ball.sety(HEIGHT / 2 - 10)
            ball.delta_y *= -1

        if ball.ycor() < -HEIGHT / 2 + 10:
            play_sound()
            ball.sety(-HEIGHT / 2 + 10)
            ball.delta_y *= -1

        if ball.xcor() > WIDTH / 2 - 10:
            ball.reset()
            player1.score += 1
            show_score(pen, player1, player2)

        if ball.xcor() < -WIDTH / 2 + 10:
            ball.reset()
            player2.score += 1
            show_score(pen, player1, player2)

        # Checking paddles and the ball collisions.
        if ball.xcor() < 0:
            paddle_ball_collisions(player1, ball)
        else:
            paddle_ball_collisions(player2, ball)

        # Computer move.
        if isinstance(player1, players.ComputerPlayer):
            player1.computer_move(ball)

        if isinstance(player2, players.ComputerPlayer):
            player2.computer_move(ball)

        # Condition of the game end and instructions to do then.
        if WIN_SCORE in (player1.score, player2.score):
            pen.clear()
            if player1.score == WIN_SCORE:
                pen.write("Player1 is a winner!", align="center", font=("Courier", 24, "normal"))
            else:
                pen.write("Player2 is a winner!", align="center", font=("Courier", 24, "normal"))
            time.sleep(5)
            break

        time.sleep(0.01)  # Thanks to that, game run same on any device.


if __name__ == '__main__':

    # Checking a platform type (Linux, Mac OS) to choose a proper play sound command.
    if sys.platform == "linux":
        PLATFORM = "linux"
    elif sys.platform == "darwin":
        PLATFORM = 'darwin'
    elif sys.platform == "windows":
        PLATFORM = 'windows'
        import winsound

    WIDTH, HEIGHT = (800, 600)
    WIN_SCORE = 11
    BALL_RADIUS = 10
    STRECH_WID = 5
    PADDLE_WIDTH = 24 * STRECH_WID

    main()
