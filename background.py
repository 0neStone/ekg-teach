import turtle
import time

class labyrinth:
    def __init__(self):
        self.drawer = turtle.Turtle()
        self.drawer.hideturtle()
        turtle.tracer(0, 0)

        self.drawer.up()
        self.x0 = -200
        self.y0 = -200
        self.stepwidth = 50
        self.borderlength = 10
        self.margin = 1
        self.besetzt = []
        self.border()
        self.gitter()
        self.beschriftungen()

    def setze(self, item, x, y):
        if item == "Stein":
            self.stein(self.x0 + x*self.stepwidth, self.y0 + y*self.stepwidth, x, y)
        elif item == "Start":
            self.end(self.x0 + x*self.stepwidth, self.y0 + y*self.stepwidth, "start")
        elif item == "Ziel":
            self.end(self.x0 + x*self.stepwidth, self.y0 + y*self.stepwidth, "ziel")
        else:
            print("Dieses item gibt es nicht!")
        turtle.update()

    def stein(self, x ,y, xx, yy):
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
        coords = [xx, yy]
        self.besetzt.append(coords)

    def end(self, x ,y, type):
        if type == "start":
            self.drawer.color("red")
        else:
            self.drawer.color("gold")
        self.drawer.goto(x + self.margin, y + self.margin)
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

class player:
    def __init__(self, x0, y0, x1, y1):
        self.schildie = turtle.Turtle()
        self.schildie.shape("turtle")
        self.schildie.up()
        self.geheZu(x0, y0)
        self.x0 = -200
        self.y0 = -200
        self.endX = x1
        self.endY = y1
        self.stepwidth = 50
        self.richtung = 1
        self.sleeptime = 1

    def geheZu(self, x, y):
        x *= laby.stepwidth
        y *= laby.stepwidth
        x += laby.stepwidth/2
        y += laby.stepwidth/2
        x += laby.x0
        y += laby.y0
        self.schildie.goto(x, y)

    def vor(self, steps):
        print(self.vorne("vor"))
        time.sleep(self.sleeptime)
        if self.vorne("vor"):
            print("Es liegt ein Stein vor dir, du kannst da nicht hingehen")
        else:
            self.schildie.forward(self.stepwidth*steps)
            turtle.update()
        if self.getposition() == [self.endX, self.endY]:
            print("Du hast es geschafft!")

    def zurueck(self, steps):
        time.sleep(self.sleeptime)
        if self.vorne("rück"):
            print("Es liegt ein Stein hinter dir, du kannst da nicht hingehen")
        else:
            self.schildie.backward(self.stepwidth*steps)
            turtle.update()

    def links(self):
        time.sleep(self.sleeptime)
        self.schildie.left(90)
        self.richtung = self.aenderausrichtung("left", self.richtung)
        turtle.update()

    def rechts(self):
        time.sleep(self.sleeptime)
        self.schildie.right(90)
        self.richtung = self.aenderausrichtung("right", self.richtung)
        turtle.update()

    def vorne(self, dir):
        time.sleep(self.sleeptime)
        eigenfeld = self.getposition()
        eigenX = eigenfeld[0]
        eigenY = eigenfeld[1]

        if dir == "vor":
            if self.richtung == 0: #oben
                vorderX = eigenX
                vorderY = eigenY + 1
            elif self.richtung == 1: #rechts
                vorderX = eigenX +1
                vorderY = eigenY
            elif self.richtung == 2: # unten
                vorderX = eigenX
                vorderY = eigenY - 1
            elif self.richtung == 3: # links
                vorderX = eigenX - 1
                vorderY = eigenY
        else:
            if self.richtung == 0: #oben
                vorderX = eigenX
                vorderY = eigenY - 1
            elif self.richtung == 1: #rechts
                vorderX = eigenX - 1
                vorderY = eigenY
            elif self.richtung == 2: # unten
                vorderX = eigenX
                vorderY = eigenY + 1
            elif self.richtung == 3: # links
                vorderX = eigenX +1
                vorderY = eigenY

        vorderCoords = [vorderX, vorderY]
        return self.besetzt(vorderX, vorderY)

    def besetzt(self, vorderX, vorderY):
        for coordinate in laby.besetzt:
            if vorderX == coordinate[0] and vorderY == coordinate[1]:
                return True
            else:
                pass
        return False

    def getposition(self):
        x = self.schildie.xcor()
        y = self.schildie.ycor()
        x -= self.stepwidth/2 # von mitte des Feldes zu Ursprung des Feldes zurück
        y -= self.stepwidth/2 #-//-
        x -= self.x0
        y -= self.y0
        x /= self.stepwidth
        y /= self.stepwidth
        return(x, y)


    def aenderausrichtung(self, dir, richtung): # 0 = up, 1 = right, 2 = down, 3 = left
        if dir == "left":
            richtung -= 1
        else:
            richtung += 1
        if richtung > 3:
            richtung = 0
        elif richtung < 0 :
            richtung = 3
        return richtung

def beispiellabyrinth(id):
    if id==1:
        for x in range(0, laby.borderlength):
            laby.setze("Stein", x, 0)
            laby.setze("Stein", x, laby.borderlength-1)
        for y in range(0, laby.borderlength):
            laby.setze("Stein", 0, y)
            laby.setze("Stein", laby.borderlength-1, y)
        laby.setze("Ziel", endX, endY)
        laby.setze("Start", startX, startY)
        for x in range(0, laby.borderlength-2):
            laby.setze("Stein", x, 2)
        for x in range(2, laby.borderlength):
            laby.setze("Stein", x, 4)
        for x in range(0, laby.borderlength-2):
            laby.setze("Stein", x, 6)
        for x in range(2, laby.borderlength):
            laby.setze("Stein", x, 8)
startX = 2
startY = 1
endX = 1
endY = 8
laby = labyrinth()
spieler = player(startX, startY, endX, endY)
