from background import *
import ui
import turtle

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
