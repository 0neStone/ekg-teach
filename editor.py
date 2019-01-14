import turtle
from background import laby, spieler
from tkinter import *

class editor():
    def __init__(self):
        self.selected = []
        self.xEnd = 0
        self.yEnd =0
        self.xStart = 0
        self.yStart = 0
        x0 = -60
        y0 = -280
        self.xBlack = x0;self.yBlack = y0
        self.xWhite = x0;self.yWhite = y0-50
        self.xStart = x0+50;self.yStart = y0
        self.xEnd = x0+50;self.yEnd = y0-50
        self.finish = turtle.Turtle();self.finish.up();self.finish.shape("triangle");self.finish.goto(self.xEnd,self.yEnd);self.finish.onclick(self.set_finish);self.finish.left(90);self.finish.color("gold")
        self.start = turtle.Turtle();self.start.up();self.start.shape("triangle");self.start.goto(self.xStart,self.yStart);self.start.onclick(self.set_start);self.start.left(90);self.start.color("red")
        self.black = turtle.Turtle();self.black.up();self.black.shape("square");self.black.goto(self.xBlack,self.yBlack);self.black.onclick(self.fill_black)
        self.whiteBorder(self.xWhite, self.yWhite)
        self.white = turtle.Turtle();self.white.up();self.white.shape("square");self.white.goto(self.xWhite,self.yWhite);self.white.onclick(self.erase);self.white.color("white")
        self.fakeTurtle = turtle.Turtle();self.fakeTurtle.up();self.fakeTurtle.shape("turtle");self.fakeTurtle.goto(x0-50,y0-50);self.fakeTurtle.onclick(self.moveTurtle)

        self.save = turtle.Turtle();self.save.up();self.save.right(90);self.save.goto(x0 - 50, y0);self.save.onclick(laby.saveMaze);self.save.pensize(3)#;save.shape('blank')
        #ts = turtle.getscreen()
        #ts.getcanvas().postscript(file="data/save.png")
        self.save.goto(x0-60, y0-7);self.save.down();self.save.forward(2);self.save.left(90);self.save.forward(20); self.save.left(90);self.save.forward(2);self.save.up();self.save.goto(x0-50, y0);self.save.left(180);self.save.turtlesize(1.5, 1.5)

        self.coords = turtle.onscreenclick(self.select)

        self.selected = []
    def fill_black(self, x, y):
        if len(self.selected) == 0:
            print("Bitte wähle ein oder mehrere Felder aus")
            return
        for i in range(0, len(self.selected)):
            laby.square(self.selected[i][0], self.selected[i][1],"white",True)
            laby.setze("Stein", self.selected[i][0], self.selected[i][1])
        self.selected = []

    def erase(self, x, y):
        if len(self.selected) == 0:
            print("Bitte wähle ein oder mehrere Felder aus")
            return
        for i in range(0, len(self.selected)):
            try:
                laby.besetzt.remove([self.selected[i][0], self.selected[i][1]])
            except ValueError:
                pass
            laby.square(self.selected[i][0], self.selected[i][1],"white",True)
        self.selected = []

    def select(self, x, y):
        x = int((x-spieler.x0)/spieler.stepwidth)
        y = int((y-spieler.y0)/spieler.stepwidth)
        for coord in self.selected:
            if coord == [x, y]:
                if coord in laby.besetzt:
                    laby.square(x,  y, "grey")
                else:
                    laby.square(x,  y, "white")
                self.selected.remove([x, y])
                return
        if x>=0 and x<=laby.borderlength-1 and y>=0 and y<=laby.borderlength-1:
            laby.square(x, y, "red")
            self.selected.append([x, y])

    def set_finish(self, x,y):
        if len(self.selected) == 0:
            print("Bitte wähle genau ein Feld aus")
            return
        elif len(self.selected) > 1:
            print("Es kann nur ein Ziel geben")
            return
        x = self.selected[0][0]
        y = self.selected[0][1]
        spieler.endX = x
        spieler.endY = y
        self.erase(x, y)
        laby.end(x, y, "ziel")
        self.selected = []

    def set_start(self, x, y):
        if len(self.selected) == 0:
            print("Bitte wähle genau ein Feld aus")
            return
        elif len(self.selected) > 1:
            print("Es kann nur einen Start geben, bitte wähle nur ein Feld aus")
            return
        x = self.selected[0][0]
        y = self.selected[0][1]
        spieler.geheZu(x, y)
        self.erase(x, y)
        laby.end(x, y, "start")
        self.selected = []

    def whiteBorder(self, x, y):
        self.black.goto(x-11,y-11)
        self.black.down()
        self.black.forward(22);self.black.left(90);self.black.forward(22);self.black.left(90);self.black.forward(22);self.black.left(90);self.black.forward(22);self.black.left(90)
        self.black.up()
        self.black.goto(self.xBlack,self.yBlack)

    def moveTurtle(self, x, y):
        if len(self.selected) == 0:
            print("Bitte wähle genau ein Feld aus")
            return
        elif len(self.selected) > 1:
            print("Es kann nur eine Turtle geben, bitte wähle nur ein Feld aus")
            return
        x = self.selected[0][0]
        y = self.selected[0][1]
        spieler.geheZu(x, y)
        self.erase(x, y)

edit0r = editor()
