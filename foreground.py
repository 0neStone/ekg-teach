from background import *
import ui

# Todo: Befehle über Input eingeben
while True:
    turtle.update()
    if not laby.paused:
        if spieler.hindernisserkennung("links"):
            if spieler.hindernisserkennung("rechts"):
                if spieler.hindernisserkennung("vorne"):
                    spieler.rechts()
                    spieler.rechts()
                spieler.vor(1)
            else:
                spieler.rechts()
        else:
            spieler.links()
            spieler.vor(1)
