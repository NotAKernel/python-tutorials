import turtle
import os

class Ball:

    def __init__(self):
        # Ball
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)

        self.ball.dx = 2
        self.ball.dy = 2


    def updatePosition(self, paddle_a, paddle_b):
        # Move the ball
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)


        # Border checking
        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.ball.dy *= -1
            # os.system("afplay bounce.wav&")

        elif self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.ball.dy *= -1
            # os.system("afplay bounce.wav&")
        
        # Paddle and ball collisions
        if self.ball.xcor() < -340 and self.ball.ycor() < paddle_a.paddle.ycor() + 50 and self.ball.ycor() > paddle_a.paddle.ycor() - 50:
            self.ball.dx *= -1.2 
            # os.system("afplay bounce.wav&")
        
        elif self.ball.xcor() > 340 and self.ball.ycor() < paddle_b.paddle.ycor() + 50 and self.ball.ycor() > paddle_b.paddle.ycor() - 50:
            self.ball.dx *= -1.2
            # os.system("afplay bounce.wav&")


    def ballGoal(self, score_a, score_b):

        # Scoring
        if self.ball.xcor() > 380:
            self.ball.goto(0, 0)
            score_a += 1
            self.ball.dx = 2
            self.ball.dx *= -1

        elif self.ball.xcor() < -380:
            self.ball.goto(0, 0)
            score_b += 1
            self.ball.dx = -2
            self.ball.dx *= -1
        