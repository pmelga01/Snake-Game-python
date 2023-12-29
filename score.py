from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
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

    def reset_score(self):
        if (self.score > self.highscore):
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    # Update scoreboard at top of screen
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}   Highscore: {self.highscore}", align="center", font=("Courier", 22, "normal"))