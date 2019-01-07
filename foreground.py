from background import *

def labyrinth():
    for x in range(0, 5):
        for y in range(0, 5):
            pass
            laby.setze("Stein", x*2+1, y*2+1)
    laby.setze("Ziel", 3, 3)
    laby.setze("Start", 5, 8)
labyrinth()
spieler.vor(1)
spieler.links()
spieler.vor(1)
print(spieler.vorne())
input()
