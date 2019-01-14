from background import *
import ui

# Todo: Befehle über Input eingeben
while True:
    turtle.update()
    if not laby.paused:
        if spieler.hinderniserkennung("links") and spieler.hinderniserkennung("rechts") and spieler.hinderniserkennung("vorne"):
            spieler.links()
            spieler.links()
        if spieler.hinderniserkennung("links"):
            if spieler.hinderniserkennung("rechts"):
                if spieler.hinderniserkennung("vorne"):
                    spieler.rechts()
                    spieler.rechts()
                spieler.vor(1)
            else:
                spieler.rechts()
        else:
            spieler.links()
            spieler.vor(1)
