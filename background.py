import turtle
import time

schildkröte = turtle.Turtle()
schildkröte.shape("turtle")
schildkröte.up()

drawer = turtle.Turtle()
drawer.hideturtle()

def vor(steps):
  schildkröte.forward(50*steps)

def zurück(steps):
    schildkröte.backward(50*steps)

def links():
    schildkröte.left(90)

def rechts():
    schildkröte.right(90)

def vorne():
    vor = True
    return True

def setze(item):
    x  = schildkröte.xcor()
    y = schildkröte.ycor()
    if item == "Stein":
        stein(x, y)
    elif item == "Start":
        start(x, y)
    elif item == "Ziel":
        ziel(x, y)
    else:
        print("Dieses item gibt es nicht!")

def stein(x ,y):
    drawer.up()
    drawer.goto(x, y)
    drawer.down()
    drawer.begin_fill()
    drawer.color("grey")
    for x in range(0, 4):
        drawer.forward(50)
        drawer.left(90)
    drawer.end_fill()
    drawer.up()

def start(x ,y):
    drawer.up()
    drawer.goto(x, y)
    drawer.down()
    drawer.begin_fill()
    drawer.color("red")
    for x in range(0, 4):
        drawer.forward(50)
        drawer.left(90)
    drawer.end_fill()
    drawer.up()

def ziel(x ,y):
    drawer.up()
    drawer.goto(x, y)
    drawer.down()
    drawer.begin_fill()
    drawer.color("gold")
    for x in range(0, 4):
        drawer.forward(50)
        drawer.left(90)
    drawer.end_fill()
    drawer.up()

setze("Stein")
vor(3)
setze("Ziel")
links()
vor(3)
setze("Start")
input()
