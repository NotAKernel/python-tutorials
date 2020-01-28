# import turtle
# import os
# from ball import Ball
# from table import Table
# from paddles import Paddle

# wn = turtle.Screen()
# wn.title("Pong")
# wn.bgcolor("black")
# wn.setup(width=800, height=600)
# wn.tracer(0)

# table = Table()
# table.__init__()

# # Score
# score_a = 0
# score_b = 0


# ball_control = Ball()

# # Paddle A
# paddle_a = Paddle((-350, 0))

# # Paddle B
# paddle_b = Paddle((350, 0))

# # Pen
# pen = turtle.Turtle()
# pen.speed(0)
# pen.color("white")
# pen.penup()
# pen.hideturtle()
# pen.goto(0, 260)
# pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# ball_control = Ball()


# # Function
# def paddle_a_up():
#     paddle_a.paddleUp()

# def paddle_a_down():
#     paddle_a.paddleDown()

# def paddle_b_up():
#     paddle_b.paddleUp()

# def paddle_b_down():
#     paddle_b.paddleDown()

# Paddle.boundaries

# # Keyboard Binding

# wn.onkey(paddle_a_up, "w")
# wn.onkey(paddle_a_down, "s")

# wn.onkey(paddle_b_up, "Up")
# wn.onkey(paddle_b_down, "Down")

# wn.listen()


# # Main game loop
# while True:
#     wn.update()


