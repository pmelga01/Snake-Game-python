# Snake Game
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import time

gameOver = False

# Initial Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#F3E7FF")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Score()
screen.listen()

# Game loop
while (not gameOver):
    screen.update()
    time.sleep(0.1)

    # Move snake directions
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    snake.move()

    # Detect collision with wall
    if (snake.head.xcor() > 280 or 
        snake.head.xcor() < -280 or 
        snake.head.ycor() > 280 or 
        snake.head.ycor() < -280):
        gameOver = True

    # Detect collision with tail (excluding head)
    for segment in snake.pieces[1:]:
        if (snake.head.distance(segment) < 15):
            gameOver = True

    # Detect collision with food
    if (snake.head.distance(food) < 20):
        scoreboard.update_score()
        food.refresh()
        snake.extend()
        snake.goFaster
    

# Game is over!
screen.update()
scoreboard.gameOver()


# So screen won't close automatically
screen.exitonclick()