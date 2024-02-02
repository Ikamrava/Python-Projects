from turtle import Screen, Turtle
from paddle import Paddle
import time

Screen = Screen()
Screen.setup(width=800, height=600)
Screen.bgcolor("black")
Screen.title("Pong")
Screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


Screen.listen()
Screen.onkey(r_paddle.go_up, "Up")
Screen.onkey(r_paddle.go_down, "Down")
Screen.onkey(l_paddle.go_up, "w")
Screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    Screen.update()




Screen.exitonclick()