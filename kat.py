import turtle as fra

from base2 import *

screen = fra.Screen()
screen.setup(500, 500)
screen.tracer(False)

# text object is for writing the text
text = fra.Turtle()
text.penup()
text.goto(-50, 200)
text.write("Welcome", font=("Arial", 20, "normal"))
text.goto(0, 200)
text.pendown()
text.goto(0, -230)

y1 = 0
y2 = 0

ball_position = Vector(0, 0)
aim = Vector(3, 5)
ball = fra.Turtle()

# Lets create our vectors
def draw():
    ball.clear()
    ball.penup()
    ball_position.move(aim)
    x = ball_position.x
    y = ball_position.y

    ball.goto(x, y)
    ball.dot(15)

    # To make it bounce, some if condition is needed

    if y > 245 or y < -245:
        aim.y = -aim.y

    if x > 215:
        high = player1.ycor()
        low = player1.ycor() - 70

        print(low, high, y)

        if y >= low and y <= high:
            aim.x = -aim.x
        else:
            text.goto(-50, 0)
            text.write("Player 2 lost", font=('Permanent Marker', 20, "normal"))

    if x < -215:
        high = player2.ycor()
        low = player2.ycor() - 70

        print(low, high, y)

        if y >= low and y <= high:
            aim.x = -aim.x
        else:
            text.goto(-50, 0)
            text.write("Player 1 lost", font=('Permanent Marker', 20, "normal"))

    screen.ontimer(draw, 50)


def rectangle(x, y, width, height, player):
    player.penup()
    player.goto(x, y)
    player.begin_fill()
    for i in range(2):
        player.right(90)
        player.forward(height)
        player.right(90)
        player. forward(width)
    player.end_fill()

def up1():
    global y1, y2
    y1 = y1 + 10
    player1.clear()
    # Right side player
    rectangle(230, y1, 10, 70, player1)

def up2():
    global y2, y1
    y2 = y2 + 10
    player2.clear()
    # left side player
    rectangle(-230, y2, 10, 70, player2)

def down1():
    global y1, y2
    y1 = y1 - 10
    player1.clear()
    # Right side player
    rectangle(230, y1, 10, 70, player1)

def down2():
    global y1, y2
    y2 = y2 - 10
    player2.clear()
    # left side player
    rectangle(-230, y2, 10, 70, player2)


#########  x   y  width height
player1 = fra.Turtle()
player2 = fra.Turtle()
rectangle(230, 0, 10, 70, player1)
rectangle(-230, 0, 10, 70, player2)



screen.onkeypress(up1, "i")
screen.onkeypress(up2, "w")
screen.onkeypress(down1, "k")
screen.onkeypress(down2, "s")

draw()



screen.listen()

fra.done()