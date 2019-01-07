from background import *

beispiellabyrinth(1)

while True:
    spieler.vor(1)
    spieler.links()
    if spieler.vorne("vor"):
        spieler.rechts()
