from turtle import Turtle, Screen
from body import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('The Pong Game')
screen.listen()
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()
ball = Ball()
screen.onkeypress(key='Up', fun=r_paddle.move_up)
screen.onkeypress(key='Down', fun=r_paddle.move_down)
screen.onkeypress(key='w', fun=l_paddle.move_up)
screen.onkeypress(key='s', fun=l_paddle.move_down)

duration = 0.1
stop = False
while not stop:
    time.sleep(duration)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_r()
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_paddle()
    if ball.xcor() > 400 and ball.distance(r_paddle) > 50:
        ball.home()
        ball.bounce_l()
        scoreboard.l_point()
        duration -= 0.01
    elif ball.xcor() < -400 and ball.distance(l_paddle) > 50:
        ball.home()
        ball.bounce_l()
        scoreboard.r_point()
        duration -= 0.01

    screen.update()



screen.exitonclick()



