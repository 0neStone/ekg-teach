from background import *
from ui import *

def laufe():
    ###Algorithmus für das Labyrinth hier rein###
    if not spieler.hinderniserkennung("links"):
        spieler.links()
    elif not spieler.hinderniserkennung("rechts"):
        spieler.rechts()
    elif spieler.hinderniserkennung("vorne"):
        spieler.umdrehen()
    spieler.vor()

init(laufe)

while True:
    update()
    if not laby.paused:
        laufe()
