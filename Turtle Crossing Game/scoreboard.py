from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 0
        self.penup()
        self.goto(y= 260, x= -260)
        self.update_writing()

    def update_writing(self):
        self.clear()
        self.write(f"Level: {self.level}", align= "left", font= FONT)
        
    def increase_level(self):
        self.level += 1
        self.update_writing()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align= "center", font= FONT)