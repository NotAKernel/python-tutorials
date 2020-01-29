# Turtle Graphics Game
import turtle
import math
import random
import os

# Set up screen
wn = turtle.Screen()
wn.bgcolor("grey")
wn.bgpic("kbgame-bg.gif")
wn.tracer(3)


# Draw border
mypen = turtle.Turtle()
mypen.color("white")
mypen.penup()
mypen.setpos(-300, -300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()


# Create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)

# Create score variable
score = 0


# Create goals
maxGoals = 6
goals = []

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setpos(random.randint(-280, 280), random.randint(-280, 280))


# Set speed variable
speed = 1

# Define functions
def turnLeft():
    player.left(20.5)

def turnRight():
    player.right(20.5)

def increaseSpeed():
    global speed
    speed += 1
    if speed > 10:
        speed = 10

def decreaseSpeed():
    global speed
    speed -= 1
    if speed < 0:
        speed = 0


def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False




# Keyboard bindings
wn.listen()
wn.onkey(turnLeft, 'Left')
wn.onkey(turnRight, 'Right')
wn.onkey(increaseSpeed, 'Up')
wn.onkey(decreaseSpeed, 'Down')

while True:
    player.forward(speed)

    # Boundary Checking
    if player.xcor()  + 10 > 300 or player.xcor() - 10 < -300:
        player.right(180)
        os.system("afplay bounce.mp3&")

    if player.ycor()  + 10 > 300 or player.ycor() - 10 < -300:
        player.right(180)
        os.system("afplay bounce.mp3&")

    for count in range(maxGoals):

        if goals[count].xcor()  + 10 > 300 or goals[count].xcor() - 10 < -300:
            goals[count].right(180)
            os.system("afplay bouncemp3&")

        if goals[count].ycor()  + 10 > 300 or goals[count].ycor() - 10 < -300:
            goals[count].right(180)
            os.system("afplay bounce.mp3&")


        # Collision checking
        if isCollision(player, goals[count]):
            goals[count].setpos(random.randint(-280, 280), random.randint(-280, 280))
            goals[count].right(random.randint(0, 360))
            os.system("afplay collision.mp3&")
            score += 1
            # Draw score
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setpos(-290, 310)
            scorestring = "Score: %s" %score
            mypen.write(scorestring, False, align= 'left', font= ("Arial", 14, "normal"))
        
            


        # Move the goal
        goals[count].forward(3)