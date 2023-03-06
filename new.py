from turtle import Turtle, Screen
import time

screen = Screen()
screen.bgcolor("black")
screen.title("The Snake Game")
screen.setup(width=600, height=600)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
snake_segments = []
screen.tracer(0)

for position in starting_positions:
    new_seg = Turtle(shape="square")
    new_seg.color("white")
    new_seg.penup()
    new_seg.setposition(position)
    snake_segments.append(new_seg)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(1)
    length_of_snake = len(snake_segments)
    for segment in range(length_of_snake - 1, 0, -1):
        x_pos = snake_segments[segment - 1].xcor()
        y_pos = snake_segments[segment - 1].ycor()
        snake_segments[segment].setposition(x=x_pos, y=y_pos)

    snake_segments[0].forward(20)
    snake_segments[0].left(90)
