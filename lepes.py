import random
import kiiras

def lepes(meret, tabla):
    sor = random.randint(0, int(meret)-1)
    oszlop = random.randint(0, int(meret)-1)
    tabla[sor][oszlop] = 'O'
    
    kiiras.palya(meret, tabla)
    
    return tabla

def jatekos_lepes(meret, tabla):
    input("Add meg a lépésed (pl. A1): ")
    i=0
    while i < 1:
        lepes = input("Add meg a lépésed (pl. A1): ")
        sor = ord(lepes[0].upper()) - 65
        oszlop = int(lepes[1:]) - 1

        if sor < 0 or sor >= meret or oszlop < 0 or oszlop >= meret:
            print("Érvénytelen lépés. Próbáld újra.")
        elif tabla[sor][oszlop] != ' ':
            print("Ez a mező már foglalt. Próbáld újra.")
        else:
            tabla[sor][oszlop] = 'X'
            i += 1
    kiiras.palya(meret, tabla)
    return tabla