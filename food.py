import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.85, stretch_wid=0.85)
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))