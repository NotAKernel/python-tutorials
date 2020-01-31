import turtle

class Pen():
    
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


    def updateScore(self, score_a, score_b):   
            self.pen.clear()
            self.pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
