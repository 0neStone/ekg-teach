import turtle
from background import laby, spieler
global selected
selected = []
def fill_black(x,y):
    global selected
    if len(selected) == 0:
        print("Bitte wähle ein oder mehrere Felder aus")
        return
    for i in range(0, len(selected)):
        laby.square(selected[i][0], selected[i][1],"white",True)
        laby.setze("Stein", selected[i][0], selected[i][1])
    selected = []
def erase(x, y):
    global selected
    if len(selected) == 0:
        print("Bitte wähle ein oder mehrere Felder aus")
        return
    for i in range(0, len(selected)):
        laby.square(selected[i][0], selected[i][1],"white",True)
        try:
            laby.besetzt.remove([selected[i][0], selected[i][1]])
        except ValueError:
            pass
    selected = []
def select(x, y):
    x = int((x-spieler.x0)/spieler.stepwidth)
    y = int((y-spieler.y0)/spieler.stepwidth)
    for coord in selected:
        if coord == [x, y]:
            if coord in laby.besetzt:
                laby.square(x,  y, "grey")
            else:
                laby.square(x,  y, "white")
            selected.remove([x, y])
            return
    if x>=0 and x<=laby.borderlength-1 and y>=0 and y<=laby.borderlength-1:
        laby.square(x, y, "red")
        selected.append([x, y])

def set_finish(x,y):
    global selected
    if len(selected) == 0:
        print("Bitte wähle genau ein Feld aus")
        return
    elif len(selected) > 1:
        print("Es kann nur ein Ziel geben")
        return
    x = selected[0][0]
    y = selected[0][1]
    spieler.endX = x
    spieler.endY = y
    erase(x, y)
    laby.end(x, y, "ziel")
    selected = []
def set_start(x, y):
    global selected
    if len(selected) == 0:
        print("Bitte wähle genau ein Feld aus")
        return
    elif len(selected) > 1:
        print("Es kann nur einen Start geben")
        return
    x = selected[0][0]
    y = selected[0][1]
    spieler.geheZu(x, y)
    erase(x, y)
    laby.end(x, y, "start")
    selected = []

def whiteBorder(x, y):
    black.goto(x-11,y-11)
    black.down()
    black.forward(22);black.left(90);black.forward(22);black.left(90);black.forward(22);black.left(90);black.forward(22);black.left(90)
    black.up()
    black.goto(xBlack,yBlack)
x0 = -60
y0 = -280
xBlack = x0;yBlack = y0
xWhite = x0;yWhite = y0-50
xStart = x0+50;yStart = y0
xEnd = x0+50;yEnd = y0-50

finish = turtle.Turtle();finish.up();finish.shape("triangle");finish.goto(xEnd,yEnd);finish.onclick(set_finish);finish.left(90);finish.color("gold")
start = turtle.Turtle();start.up();start.shape("triangle");start.goto(xStart,yStart);start.onclick(set_start);start.left(90);start.color("red")
black = turtle.Turtle();black.up();black.shape("square");black.goto(xBlack,yBlack);black.onclick(fill_black)
whiteBorder(xWhite, yWhite)
white = turtle.Turtle();white.up();white.shape("square");white.goto(xWhite,yWhite);white.onclick(erase);white.color("white")

save = turtle.Turtle();save.up();save.shape("square");save.goto(x0 - 50, y0);save.onclick(laby.saveMaze)

coords = turtle.onscreenclick(select)
