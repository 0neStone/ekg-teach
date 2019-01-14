import foreground
import ui
import turtle
from background import laby, spieler

x=0
while True:
    turtle.update()
    if not laby.paused:
        print(spieler.hinderniserkennung("vorne"))
        foreground.laufe()
