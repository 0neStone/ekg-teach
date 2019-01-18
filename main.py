import foreground
from ui import *
import turtle
from background import laby, spieler

x=0
while True:
    turtle.update()
    #turtle.onscreenclick(editor.edit0r.saveMaze)
    if not laby.paused:
        spieler.hinderniserkennung("vorne")
        foreground.laufe2()
