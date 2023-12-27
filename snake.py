from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.pieces = []
        self.create_snake()
        self.head = self.pieces[0]
    
    def create_snake(self):
        for i in range(3):
            segment = Turtle()
            segment.penup()
            segment.goto(i * -20, 0)
            segment.shape("square")
            segment.color("white")
            self.pieces.append(segment)
    
    def move(self):
        for seg in range(len(self.pieces) - 1, 0, -1):
            self.pieces[seg].goto(self.pieces[seg-1].xcor(), self.pieces[seg-1].ycor())
        
        self.head.forward(MOVE_DISTANCE)
    
    def left(self):
        if (self.head.heading() != RIGHT):
            self.head.setheading(LEFT)
    
    def right(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)
    
    def up(self):
        if (self.head.heading() != DOWN):
            self.head.setheading(UP)

    def down(self):
        if (self.head.heading() != UP):
            self.head.setheading(DOWN)
