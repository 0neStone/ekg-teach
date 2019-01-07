import turtle
import time

class labyrinth():
    def __init__(self):
        self.drawer = turtle.Turtle()
        self.drawer.hideturtle()
        self.drawer.speed(100)

        self.drawer.up()
        self.x0 = -200
        self.y0 = -200
        self.stepwidth = 50
        self.borderlength = 10
        self.margin = 1
        self.border()
        self.gitter()
        self.beschriftungen()

    def setze(self, item, x, y):
        if item == "Stein":
            self.stein(self.x0 + x*self.stepwidth, self.y0 + y*self.stepwidth)
        elif item == "Start":
            self.end(self.x0 + x*self.stepwidth, self.y0 + y*self.stepwidth, "start")
        elif item == "Ziel":
            self.end(self.x0 + x*self.stepwidth, self.y0 + y*self.stepwidth, "ziel")
        else:
            print("Dieses item gibt es nicht!")

    def stein(self, x ,y):
        self.drawer.up()
        self.drawer.goto(x+self.margin, y+self.margin)
        self.drawer.down()
        self.drawer.begin_fill()
        self.drawer.color("grey")
        self.drawer.goto(x + self.stepwidth-self.margin, y+self.margin)
        self.drawer.goto(x + self.stepwidth-self.margin, y + self.stepwidth-self.margin)
        self.drawer.goto(x+ self.margin, y + self.stepwidth - self.margin)
        self.drawer.goto(x + self.margin, y + self.margin)
        self.drawer.end_fill()
        self.drawer.up()

    def end(self, x ,y, type):
        if type == "start":
            self.drawer.color("red")
        else:
            self.drawer.color("gold")
        self.drawer.goto(x, y)
        self.drawer.down()
        self.drawer.begin_fill()
        self.drawer.goto(x + self.stepwidth - self.margin, y +self.margin)
        self.drawer.goto(x + self.stepwidth/2, y+self.stepwidth - self.margin)
        self.drawer.goto(x + self.margin, y + self.margin)
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

    def beschriftungen(self):
        self.drawer.goto(self.x0, self.y0)
        self.drawer.color("black")
        for x in range(0, self.borderlength):
            self.drawer.goto(self.x0+(x+0.5)*self.stepwidth, self.y0-self.stepwidth/2)
            self.drawer.write(x, font=("Arial", 10))
        self.drawer.right(90)
        for y in range(0, self.borderlength):
            self.drawer.goto(self.x0-self.stepwidth/2, self.y0+(y+0.5)*self.stepwidth)
            self.drawer.write(y, font=("Arial", 10))
        self.drawer.up()

class player():
    def __init__(self):
        self.schildie = turtle.Turtle()
        self.schildie.shape("turtle")
        self.schildie.up()
        self.stepwidth = 50

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
        return vor

laby = labyrinth()
spieler = player()
