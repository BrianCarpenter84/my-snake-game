from turtle import Turtle
ALIGN = "center"
FONT = ("arial", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("green")
        self.penup()
        self.speed("fastest")
        self.goto(0,265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGN, font=FONT)

    def increase_score(self):
        self.clear()
        self.score +=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", move=False, align=ALIGN, font=FONT)







