import turtle
import os
from ball import *
from paddle0 import *
from pen0 import *
from table import *

# Main game class, to import into pong2.py
class Game():
    
    def __init__(self):
        
        # Window Creation
        self.window = turtle.Screen()
        self.window.title("Pong")
        self.window.bgcolor("black")
        self.window.setup(width=800, height=600)
        self.window.tracer(0)

        # Table
        table = Table()
        
        # Scores
        self.score_a = 0
        self.score_b = 0
        
        # Paddles
        self.paddle_a = Paddle((-350, 0))
        self.paddle_b = Paddle((350, 0))

        # Ball
        self.ball = Ball()

        # Pen
        self.pen = Pen()

    # Main game loop & bindings
    def run(self):
        self.window.listen()
        self.window.onkey(self.paddle_a.paddleUp, "s")
        self.window.onkey(self.paddle_a.paddleDown, "z")
        
        
        self.window.onkey(self.paddle_b.paddleUp, "Up")
        self.window.onkey(self.paddle_b.paddleDown, "Down")
        
        
        while True:
            self.window.update()
            self.ball.updatePosition(self.paddle_a, self.paddle_b)
            updated_a, updated_b = self.ball.scoreUpdate(self.score_a, self.score_b, self.pen)

            if self.score_a != updated_a or self.score_b != updated_b:
                self.score_a = updated_a
                self.score_b = updated_b
                self.pen.updateScore(self.score_a, self.score_b)

