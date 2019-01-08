from background import *
from ui import UI

UI(0, -300)
beispiellabyrinth(1)
while True:
    turtle.update()
    if spieler.hindernisserkennung("links"):
        if spieler.hindernisserkennung("rechts"):
            spieler.vor(1)
        else:
            spieler.rechts()
    else:
        spieler.links()
        spieler.vor(1)
