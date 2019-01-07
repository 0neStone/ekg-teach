from background import *

def labyrinth():
    for x in range(0, 5):
        for y in range(0, 5):
            laby.setze("Stein", x, y)
    laby.setze("Ziel", 3, 3)
    laby.setze("Start", 5, 8)
labyrinth()
input()
