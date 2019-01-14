from background import laby, spieler
import turtle
import editor

class UI:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vor = turtle.Turtle()
        self.rueck = turtle.Turtle()
        self.links = turtle.Turtle()
        self.rechts = turtle.Turtle()
        self.plus0 = turtle.Turtle()
        self.plus1 = turtle.Turtle()
        self.plus2 = turtle.Turtle()
        self.plus3 = turtle.Turtle()
        self.plus4 = turtle.Turtle()
        self.minus0 = turtle.Turtle()
        self.minus1 = turtle.Turtle()
        self.minus2 = turtle.Turtle()
        self.pause0 = turtle.Turtle()
        self.pause1 = turtle.Turtle()
        self.pause2 = turtle.Turtle()
        self.play = turtle.Turtle()
        self.play.hideturtle()
        self.vor.shape("arrow")
        self.rueck.shape("arrow")
        self.links.shape("arrow")
        self.rechts.shape("arrow")
        self.vor.up()
        self.rueck.up()
        self.links.up()
        self.rechts.up()
        self.vor.goto(self.x ,self.y)
        self.rueck.goto(self.x ,self.y)
        self.links.goto(self.x ,self.y)
        self.rechts.goto(self.x ,self.y)
        self.vor.left(90)
        self.rueck.left(270)
        self.links.left(180)
        self.vor.forward(25)
        self.rueck.forward(25)
        self.links.forward(25)
        self.rechts.forward(25)
        self.vor.turtlesize(2)
        self.rueck.turtlesize(2)
        self.links.turtlesize(2)
        self.rechts.turtlesize(2)
        self.speed(self.x+100, self.y)
        self.pause(self.x+170, self.y)
        self.go()
        self.paused = False

        self.vor.onclick(self.eventVor)
        self.rueck.onclick(self.eventZurueck)
        self.links.onclick(self.eventLinks)
        self.rechts.onclick(self.eventRechts)
        self.plus0.onclick(self.eventIncreaseSpeed)
        self.plus1.onclick(self.eventIncreaseSpeed)
        self.plus2.onclick(self.eventIncreaseSpeed)
        self.plus3.onclick(self.eventIncreaseSpeed)
        self.plus4.onclick(self.eventIncreaseSpeed)
        self.minus0.onclick(self.eventIncreaseSpeed)
        self.minus1.onclick(self.eventDecreaseSpeed)
        self.minus2.onclick(self.eventDecreaseSpeed)

        wn = turtle.Screen()
        wn.onkey(self.eventVor, "Up")
        wn.onkey(self.eventLinks, "Left")
        wn.onkey(self.eventRechts, "Right")
        wn.onkey(self.eventZurueck, "Down")
        wn.onkey(self.switch, "space")
        wn.listen()

    def eventVor(self, a=0, b=0):
        spieler.vor(1)

    def eventZurueck(self, a=0, b=0):
        spieler.zurueck(1)

    def eventLinks(self, a=0, b=0):
        spieler.links()

    def eventRechts(self, a=0, b=0):
        spieler.rechts()

    def eventIncreaseSpeed(self, a=0, b=0):
        spieler.increaseSpeed()

    def eventDecreaseSpeed(self, a=0, b=0):
        spieler.decreaseSpeed()

    def switch(self):
        if self.paused:
            self.goOn()
        else:
            self.stop()

    def stop(self, a=0, b=0):
        self.paused = True
        self.x = False
        self.switchPause()
        laby.paused = True

    def goOn(self, a=0, b=0):
        self.paused = False
        self.x = True
        self.switchPause()
        laby.paused = False

    def switchPause(self):
        if self.paused:
            self.play.showturtle()
            self.pause0.hideturtle()
            self.pause1.hideturtle()
            self.pause2.hideturtle()
            turtle.update()
        else:
            self.play.hideturtle()
            self.pause0.showturtle()
            self.pause1.showturtle()
            self.pause2.showturtle()
            turtle.update()

    def go(self):
        self.play.up()
        self.play.shape("arrow")
        self.play.turtlesize(2, 3)
        self.play.goto(self.x+170, self.y)
        self.play.onclick(self.goOn)

    def pause(self, x, y):
        self.pause0.up()
        self.pause0.shape("square")
        self.pause0.turtlesize(0.5, 2)
        self.pause0.left(90)
        self.pause0.goto(x, y)
        self.pause1.up()
        self.pause1.shape("square")
        self.pause1.color("white")
        self.pause1.turtlesize(0.5, 2)
        self.pause1.left(90)
        self.pause1.goto(x+15, y)
        self.pause2.up()
        self.pause2.shape("square")
        self.pause2.turtlesize(0.5, 2)
        self.pause2.left(90)
        self.pause2.goto(x+20, y)
        self.pause0.onclick(self.stop)
        self.pause1.onclick(self.stop)
        self.pause2.onclick(self.stop)

    def speed(self, x, y):
        laby.drawer.goto(x-160, y-70)
        self.plus0.shape("square")
        self.plus1.shape("square")
        self.plus2.shape("square")
        self.plus3.shape("square")
        self.plus4.shape("square")
        self.plus0.up()
        self.plus1.up()
        self.plus2.up()
        self.plus3.up()
        self.plus4.up()
        self.plus0.goto(x-25, y)
        self.plus1.goto(x-25, y)
        self.plus2.goto(x-25, y)
        self.plus3.goto(x-25, y)
        self.plus4.goto(x-25, y)
        self.plus1.forward(10)
        self.plus2.left(90)
        self.plus2.forward(10)
        self.plus3.left(180)
        self.plus3.forward(10)
        self.plus4.left(270)
        self.plus4.forward(10)

        self.minus0.shape("square")
        self.minus1.shape("square")
        self.minus2.shape("square")
        self.minus0.up()
        self.minus1.up()
        self.minus2.up()
        self.minus0.goto(x+25, y)
        self.minus1.goto(x+25, y)
        self.minus2.goto(x+25, y)
        self.minus1.forward(10)
        self.minus2.backward(10)

gui = UI(100, -300)
