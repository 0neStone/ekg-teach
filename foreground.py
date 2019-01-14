from background import *

# Todo: Befehle über Input eingeben


def laufe():
    if not spieler.hinderniserkennung("links"):
        spieler.links()
        spieler.vor()
    elif not spieler.hinderniserkennung("vorne"):
        spieler.vor()
    elif not spieler.hinderniserkennung("rechts"):
        spieler.rechts()
        spieler.vor()
    else:
        spieler.umdrehen()
        spieler.vor()
