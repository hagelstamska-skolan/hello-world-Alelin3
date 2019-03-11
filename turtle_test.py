import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.tracer(3)

# Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)

# Create goals
maxGoals = 6
goals = []

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(110, -110)


speed = 1

# Define functions
def turnleft():
    player.left(30)
    
def turnright():
    player.right(30)
    
def increasespeed():
    global speed
    speed += 1

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False

# Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")

restart = "Yes"
points = 0

while restart == "Yes":
    player.forward(speed)
    
    # Boundary Checking
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
    
    # Boundary Checking
    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)
    
    # Move the goal
    for count in range(maxGoals):
        goals[count].forward(3)

        # Boundary Checking
        if goals[count].xcor() > 290 or goals[count].xcor() < -290:
            goals[count].right(180)
        
        # Boundary Checking
        if goals[count].ycor() > 290 or goals[count].ycor() < -290:
            goals[count].right(180)
    
        # Collision checking
        if isCollision(player, goals[count]):
            goals[count].setposition(random.randint(-290, 290), random.randint(-290, 290))
            goals[count].right(random.randint(0, 360))
            points += 1
    if points == 20:
        print("You got 20 points")
        restart = input("Do you want to continue the game? Yes or No ")
        if restart == "Yes":
            points = 0
        else:
            print("Thanks for Playing! You can now close the game.")