# Snake Game
from turtle import Turtle, Screen
from snake import Snake
import time

# Initial Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
screen.listen()



while (True):
    screen.update()
    time.sleep(0.1)

    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    snake.move()

# screen.listen()
# screen.onkey(moveRight, "d")
# screen.onkey(moveLeft, "a")




# So screen won't close automatically
screen.exitonclick()