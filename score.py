from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("#404085")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    # Game Over message at center of screen, triggered when player loses
    def gameOver(self):
        self.penup()
        self.goto(0,0)
        self.write(f"GAME OVER!", align="center", font=("Courier", 22, "normal"))

    # Update scoreboard at top of screen
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Courier", 22, "normal"))