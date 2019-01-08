from background import laby, spieler
import turtle

class UI:
    def __init__(self, x, y):
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
        self.vor.shape("arrow")
        self.rueck.shape("arrow")
        self.links.shape("arrow")
        self.rechts.shape("arrow")
        self.vor.up()
        self.rueck.up()
        self.links.up()
        self.rechts.up()
        self.vor.goto(x ,y)
        self.rueck.goto(x ,y)
        self.links.goto(x ,y)
        self.rechts.goto(x ,y)
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
        self.speed(x+100, y)

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

        while True:
            turtle.update()

    def eventVor(self, a, b):
        spieler.vor(1)

    def eventZurueck(self, a, b):
        spieler.zurueck(1)

    def eventLinks(self, a, b):
        spieler.links()

    def eventRechts(self, a, b):
        spieler.rechts()

    def eventIncreaseSpeed(self, a, b):
        spieler.increaseSpeed()

    def eventDecreaseSpeed(self, a, b):
        spieler.decreaseSpeed()

    def init():
        pass

    def speed(self, x, y):
        laby.drawer.goto(x-170, y-60)
        laby.drawer.write("Steure die Turtle und verändere ihre Geschwindigkeit", font=("TimesNewRoman, 10"))
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

if __name__ == "__main__":
    gui = UI(0, -300)
