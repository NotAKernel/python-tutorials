import turtle

class Table:
    def __init__(self):

        # Table
        mid_line = turtle.Turtle()
        mid_line.shape("square")
        mid_line.color("red")
        mid_line.shapesize(stretch_len= 0.1, stretch_wid= 30)

        top_line = turtle.Turtle()
        top_line.shape("square")
        top_line.color("red")
        top_line.shapesize(stretch_len= 40, stretch_wid= 0.5)
        top_line.goto(0, 300)

        bottom_line = turtle.Turtle()
        bottom_line.shape("square")
        bottom_line.color("red")
        bottom_line.shapesize(stretch_len= 40, stretch_wid= 0.5)
        bottom_line.goto(0, -300)

        out_circle = turtle.Turtle()
        out_circle.shape("circle")
        out_circle.color("blue")
        out_circle.fillcolor("black")
        out_circle.shapesize(stretch_len= 10, stretch_wid= 10)

        in_circle = turtle.Turtle()
        in_circle.shape("circle")
        in_circle.color("red")
        in_circle.fillcolor("blue")
        in_circle.shapesize(stretch_len= 3, stretch_wid= 3)