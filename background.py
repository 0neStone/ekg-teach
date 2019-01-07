import turtle
import time

class background():
    def __init__(self):
        self.schildie = turtle.Turtle()
        self.schildie.shape("turtle")
        self.schildie.up()

        self.drawer = turtle.Turtle()
        self.drawer.hideturtle()
        self.drawer.speed(100)

        self.drawer.up()
        self.x0 = -200
        self.y0 = -200
        self.stepwidth = 50
        self.borderlength = 10
        self.border()
        self.gitter()

    def vor(self, steps):
      self.schildie.forward(self.stepwidth*steps)

    def zurück(self, steps):
        self.schildie.backward(self.stepwidth*steps)

    def links(self):
        self.schildie.left(90)

    def rechts(self):
        self.schildie.right(90)

    def vorne(self):
        vor = True
        return True

    def setze(self, item):
        x  = self.schildie.xcor()
        y = self.schildie.ycor()
        if item == "Stein":
            self.stein(x, y)
        elif item == "Start":
            self.start(x, y)
        elif item == "Ziel":
            self.ziel(x, y)
        else:
            print("Dieses item gibt es nicht!")

    def stein(self, x ,y):
        self.drawer.up()
        self.drawer.goto(x, y)
        self.drawer.down()
        self.drawer.begin_fill()
        self.drawer.color("grey")
        for x in range(0, 4):
            self.drawer.forward(self.stepwidth)
            self.drawer.left(90)
        self.drawer.end_fill()
        self.drawer.up()

    def start(self, x ,y):
        self.drawer.goto(x, y)
        self.drawer.down()
        self.drawer.begin_fill()
        self.drawer.color("red")
        self.drawer.goto(x + self.stepwidth, y)
        self.drawer.goto(x + self.stepwidth/2, y+self.stepwidth)
        self.drawer.goto(x, y)
        self.drawer.end_fill()
        self.drawer.up()

    def ziel(self, x ,y):
        self.drawer.goto(x, y)
        self.drawer.down()
        self.drawer.begin_fill()
        self.drawer.color("gold")
        self.drawer.goto(x + self.stepwidth, y)
        self.drawer.goto(x + self.stepwidth/2, y+self.stepwidth)
        self.drawer.goto(x, y)
        self.drawer.end_fill()
        self.drawer.up()

    def border(self):
        self.drawer.goto(self.x0, self.y0)
        self.drawer.down()
        self.drawer.color("black")
        for x in range(0, 4):
            self.drawer.forward(self.borderlength*self.stepwidth)
            self.drawer.left(90)
        self.drawer.up()

    def gitter(self):
        self.drawer.goto(self.x0, self.y0)
        self.drawer.color("#666666")
        self.drawer.left(90)
        for x in range(0, self.borderlength):
            self.drawer.up()
            self.drawer.goto(self.x0+x*self.stepwidth, self.y0)
            self.drawer.down()
            self.drawer.forward(self.borderlength*self.stepwidth)
        self.drawer.right(90)
        for y in range(0, self.borderlength):
            self.drawer.up()
            self.drawer.goto(self.x0, self.y0+y*self.stepwidth)
            self.drawer.down()
            self.drawer.forward(self.borderlength*self.stepwidth)
        self.drawer.up()



b = background()
b.setze("Stein")
b.vor(3)
b.setze("Ziel")
b.links()
b.vor(3)
b.setze("Start")
input()
