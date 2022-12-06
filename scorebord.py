from turtle import Turtle
FONT=("Courien",20,"bold")

class Score(Turtle):
    def __init__(self,totalife) -> None:
        super().__init__()
        self.score=totalife
        self.penup()
        self.goto(-250,225)
        self.fillcolor("black")
        self.pendown()
        self.forward(500)
        self.left(90)
        self.forward(23)
        self.left(90)
        self.forward(500)
        self.left(90)
        self.forward(23)
        self.penup()
        self.setheading(0)
        self.goto(0,233)
        self.color("Crimson")
        self.write(f"YOU HAVE {self.score} LIFE",align="center", font=FONT)
        self.hideturtle()
        
