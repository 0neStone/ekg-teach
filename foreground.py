from background import *

def laufe():
    if spieler.hinderniserkennung("links"):
        if spieler.hinderniserkennung("vorne"):
            if spieler.hinderniserkennung("rechts"):
                    spieler.umdrehen()
            else:
                spieler.rechts()
                spieler.vor()
        else:
            spieler.vor()
    else:
        spieler.links()
        spieler.vor()

def laufe2():
    if not spieler.hinderniserkennung("links"):
        spieler.links()
    elif not spieler.hinderniserkennung("rechts"):
        spieler.rechts()
    elif spieler.hinderniserkennung("vorne"):
        spieler.umdrehen()
    spieler.vor()

def laufe3():
    if spieler.hinderniserkennung("vorne"):
        if spieler.hinderniserkennung("rechts"):
            if spieler.hinderniserkennung("links"):
                spieler.umdrehen()
            else:
                spieler.links()
                print("links")
        else:
            spieler.rechts()
            print("rechts")
    else:
        spieler.vor()
        print("vor")
