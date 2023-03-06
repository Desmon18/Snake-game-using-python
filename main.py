from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# snake_body = []
# x_cor = 0
# y_cor = 0
screen.tracer(0)
game_is_on = True
user_score = 0

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for segment in snake_body:
    #     segment.forward(20)
    snake.move()

    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        user_score += 1
        scoreboard.update_scoreboard(user_score)

    # detect collision with walls
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -295 or snake.snake_head.ycor() > 280 or \
            snake.snake_head.ycor() < -280:
        # game_is_on = False
        # score.game_over()
        scoreboard.reset_score(user_score)
        user_score = 0
        snake.reset_snake()

    # detect collision with tail of snake
    for segment in snake.snake_segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset_score(user_score)
            user_score = 0
            snake.reset_snake()


screen.exitonclick()
