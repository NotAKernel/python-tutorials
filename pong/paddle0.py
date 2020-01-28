import turtle

class Paddle:

    def __init__(self, starting_pos):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(starting_pos[0], starting_pos[1])

    def paddleUp(self):
        y = self.paddle.ycor()
        y += 20
        self.paddle.sety(y)

    def paddleDown(self):
        y = self.paddle.ycor()
        y -= 20
        self.paddle.sety(y)