from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-230, 270)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def show_game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
