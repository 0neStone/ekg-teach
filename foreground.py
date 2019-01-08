from background import *
from ui import UI

beispiellabyrinth(1)
while True:
    if spieler.hindernisserkennung("links"):
        if spieler.hindernisserkennung("rechts"):
            spieler.vor(1)
        else:
            spieler.rechts()
    else:
        spieler.links()
        spieler.vor(1)
