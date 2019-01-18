import turtle
import time
import random

class labyrinth:
    def __init__(self):
        self.drawer = turtle.Turtle()
        self.drawer.hideturtle()
        self.drawer.speed(10)
        turtle.tracer(0, 0)

        self.drawer.up()
        self.x0 = -200
        self.y0 = -200
        self.stepwidth = 50
        self.borderlength = 10
        self.margin = 1
        self.besetzt = []
        self.startSet = False
        self.startCoords = []
        self.endSet = False
        self.endCoords = []
        self.paused = False

        try: # loading saved maze
            with open('data/besetzt.txt', 'r') as besetzt:
                lines = besetzt.readlines()
                for coord in lines:
                    coord = coord.split(";")
                    self.setze("Stein", int(coord[0]), int(coord[1]))
            with open('data/start.txt', 'r') as start:
                lines = start.readlines()
                for coord in lines:
                    coord = coord.split(";")
                    self.setze("Start", int(coord[0]), int(coord[1]))
            with open('data/end.txt', 'r') as end:
                lines = end.readlines()
                for coord in lines:
                    coord = coord.split(";")
                    self.setze("Ziel", int(coord[0]), int(coord[1]))
        except:
            self.beispiellabyrinth(1)

        self.border()
        self.gitter()
        self.beschriftungen()

    def setze(self, item, x, y):
        if item == "Stein":
            self.stein(x, y)
        elif item == "Start":
            self.end(x, y, "start")
        elif item == "Ziel":
            self.end(x, y, "ziel")
        else:
            print("Dieses item gibt es nicht!")
        turtle.update()

    def stein(self, x ,y):
        self.besetzt.append([x,y])
        x = self.x0 + x*self.stepwidth
        y = self.y0 + y*self.stepwidth
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

    def square(self, x, y, color,fill = False):
        x = self.x0 + x*self.stepwidth
        y = self.y0 + y*self.stepwidth
        self.drawer.up()
        self.drawer.goto(x+self.margin, y+self.margin)
        self.drawer.down()
        self.drawer.color(color)
        if fill == True:
            self.drawer.fillcolor(color)
            self.drawer.begin_fill()
        self.drawer.goto(x + self.stepwidth-self.margin, y+self.margin)
        self.drawer.goto(x + self.stepwidth-self.margin, y + self.stepwidth-self.margin)
        self.drawer.goto(x+ self.margin, y + self.stepwidth - self.margin)
        self.drawer.goto(x + self.margin, y + self.margin)
        self.drawer.up()
        if fill == True:
            self.drawer.end_fill()
        coords = [x, y]
        if color == "white":
            if coords in self.besetzt:
                self.besetzt.remove(coords)
        else:
            self.besetzt.append(coords)

    def geheZu(self, x, y):
        x *= self.stepwidth
        y *= self.stepwidth
        x += self.stepwidth/2
        y += self.stepwidth/2
        x += self.x0
        y += self.y0
        self.drawer.goto(x, y)

    def end(self, x ,y, type):
        if type == "start":
            if self.startSet:
                self.square(self.startCoords[0], self.startCoords[1], "white", True)
                self.square(x, y, "white", True)
            self.drawer.color("red")
            self.startSet = True
            self.startCoords = [x, y]
        elif type == "ziel":
            if self.endSet:
                self.square(self.endCoords[0], self.endCoords[1], "white", True)
                self.square(x, y, "white", True)
            self.drawer.color("gold")
            self.endSet = True
            self.endCoords = [x, y]
        x = self.x0 + x*self.stepwidth
        y = self.y0 + y*self.stepwidth
        self.drawer.up()
        self.drawer.goto(x+self.margin, y+self.margin)
        self.drawer.down()
        self.drawer.begin_fill()
        self.drawer.goto(x + self.stepwidth - self.margin, y +self.margin)
        self.drawer.goto(x + self.stepwidth/2, y+self.stepwidth - self.margin)
        self.drawer.goto(x + self.margin, y + self.margin)
        self.drawer.end_fill()
        self.drawer.up()

    def erase(self, coords):
        self.geheZu(coords[0], coords[1])
        self.drawer.color("white")
        self.drawer.begin_fill()
        self.drawer.goto(coords[0] + self.stepwidth - self.margin, coords[1] +self.margin)
        self.drawer.goto(coords[0] + self.stepwidth/2, coords[1]+self.stepwidth - self.margin)
        self.drawer.goto(coords[0] + self.margin, coords[1] + self.margin)
        self.drawer.end_fill()
        self.drawer.up()


    def border(self):
        self.drawer.pensize(2)
        self.drawer.goto(self.x0, self.y0)
        self.drawer.down()
        self.drawer.color("black")
        for x in range(0, 4):
            self.drawer.forward(self.borderlength*self.stepwidth)
            self.drawer.left(90)
        self.drawer.up()
        self.drawer.pensize(1)

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

    def saveMaze(self):
        print("Labyrinth gespeichert")
        with open("data/besetzt.txt", "w") as besetzt_file:
            for i in range(0,len(laby.besetzt)):
                besetzt_file.write(str(laby.besetzt[i][0]) + ";" + str(laby.besetzt[i][1])+ "\n")
        with open("data/start.txt", "w") as start_file:
            try:
                start_file.write(str(laby.startCoords[0]) + ";" + str(laby.startCoords[1])+ "\n")
            except IndexError:
                pass
        with open("data/end.txt","w") as end_file:
            try:
                end_file.write(str(laby.endCoords[0]) + ";" + str(laby.endCoords[1])+ "\n")
            except IndexError:
                pass

    def beispiellabyrinth(self, id):
        if id==1:
            for x in range(0, self.borderlength):
                self.setze("Stein", x, 0)
                self.setze("Stein", x, self.borderlength-1)
            for y in range(0, self.borderlength):
                self.setze("Stein", 0, y)
                self.setze("Stein", self.borderlength-1, y)
            self.setze("Ziel", 8, 8)
            self.setze("Start", 1, 1)
            for x in range(0, self.borderlength-2):
                self.setze("Stein", x, 2)
            for x in range(2, self.borderlength):
                self.setze("Stein", x, 4)
            for x in range(0, self.borderlength-2):
                self.setze("Stein", x, 6)
            for x in range(2, self.borderlength):
                self.setze("Stein", x, 8)


class player():
    def __init__(self):
        self.schildie = turtle.Turtle()
        self.schildie.shape("turtle")
        self.schildie.up()
        self.geheZu(laby.startCoords[0], laby.startCoords[1])
        self.x0 = -200
        self.y0 = -200
        self.endX = laby.endCoords[0]
        self.endY = laby.endCoords[1]
        self.stepwidth = 50
        self.richtung = 1
        self.sleeptime = 0.1

    def geheZu(self, x, y):
        x *= laby.stepwidth
        y *= laby.stepwidth
        x += laby.stepwidth/2
        y += laby.stepwidth/2
        x += laby.x0
        y += laby.y0
        self.schildie.goto(x, y)

    def vor(self, steps=1):
        posX, posY = self.getposition()
        vorderCoords = self.vorderCoord(posX, posY, "vorne")
        x = vorderCoords[0]
        y = vorderCoords[1]
        if x>=0 and x<=laby.borderlength-1 and y>=0 and y<=laby.borderlength-1:
            if self.getposition()[0] == self.endX and self.getposition()[1] == self.endY:
                print("Sie haben ihr Ziel erreicht! Das Ziel liegt auf der", "rechten" if random.randint(0,1)==0 else "linken","Seite")
                self.ende()
            time.sleep(self.sleeptime)
            if self.hinderniserkennung("vorne"):
                pass
                '''print("Es liegt ein Stein vor dir, du kannst da nicht hingehen")'''
            else:
                for x in range(0, steps):
                    self.schildie.forward(self.stepwidth)
                turtle.update()
        else:
            return

    def zurueck(self, steps):
        time.sleep(self.sleeptime)
        if self.hinderniserkennung("hinten"):
            pass
            #print("Es liegt ein Stein hinter dir, du kannst da nicht hingehen")
        else:
            for x in range(0, steps):
                self.schildie.backward(self.stepwidth)
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

    def umdrehen(self):
        self.rechts()
        self.rechts()
        turtle.update

    def vorderCoord(self, eigenX, eigenY, dir):
        if dir == "vorne":
            if self.richtung == 0: #oben
                vorderX = eigenX
                vorderY = eigenY + 1
            elif self.richtung == 1: #rechts
                vorderX = eigenX + 1
                vorderY = eigenY
            elif self.richtung == 2: # unten
                vorderX = eigenX
                vorderY = eigenY - 1
            elif self.richtung == 3: # links
                vorderX = eigenX - 1
                vorderY = eigenY
        elif dir=="hinten":
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
                vorderX = eigenX + 1
                vorderY = eigenY
        elif dir=="links":
            if self.richtung == 0: #oben
                vorderX = eigenX -1
                vorderY = eigenY
            elif self.richtung == 1: #rechts
                vorderX = eigenX
                vorderY = eigenY + 1
            elif self.richtung == 2: # unten
                vorderX = eigenX + 1
                vorderY = eigenY
            elif self.richtung == 3: # links
                vorderX = eigenX
                vorderY = eigenY - 1
        elif dir=="rechts":
            if self.richtung == 0: #oben
                vorderX = eigenX + 1
                vorderY = eigenY
            elif self.richtung == 1: #rechts
                vorderX = eigenX
                vorderY = eigenY - 1
            elif self.richtung == 2: # unten
                vorderX = eigenX  - 1
                vorderY = eigenY
            elif self.richtung == 3: # links
                vorderX = eigenX
                vorderY = eigenY + 1
        else:
            return [-10, -10]
        return [int(vorderX), int(vorderY)]

    def hinderniserkennung(self, dir):
        time.sleep(self.sleeptime)
        eigenfeld = self.getposition()
        eigenX = eigenfeld[0]
        eigenY = eigenfeld[1]
        vorderCoords = self.vorderCoord(eigenX, eigenY, dir)
        x = vorderCoords[0]
        y = vorderCoords[1]
        #print(vorderCoords)
        if x>=0 and x<=laby.borderlength-1 and y>=0 and y<=laby.borderlength-1:
            self.schildie.goto(round(self.schildie.xcor(), 1), round(self.schildie.ycor(), 1))
            return self.test(vorderCoords[0], vorderCoords[1])
        else:
            return True

    def test(self, vorderX, vorderY):
        for coordinate in laby.besetzt:
            if vorderX == coordinate[0] and vorderY == coordinate[1]:
                return True
        return False

    def ende(self):
        while self.getposition()[0] == self.endX and self.getposition()[1] == self.endY:
            self.sleeptime = 0.5
            self.links()
        return

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

    def increaseSpeed(self):
        if self.sleeptime > 0.01:
            self.sleeptime -= 0.01


    def decreaseSpeed(self):
        self.sleeptime += 0.01







laby = labyrinth()
spieler = player()
