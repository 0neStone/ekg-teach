from ui import *
import turtle
from background import *

while True:
    turtle.update()
    go()
    if not laby.paused:
        if not spieler.hinderniserkennung("links"):
            spieler.links()
        elif not spieler.hinderniserkennung("rechts"):
            spieler.rechts()
        elif spieler.hinderniserkennung("vorne"):
            spieler.umdrehen()
        spieler.vor()
