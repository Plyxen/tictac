import random
import kiiras

def lepes(meret):
    gep_lepes=[]
    sor = random.randint(0, int(meret)-1)
    gep_lepes.append(sor)
    oszlop = random.randint(0, int(meret)-1)
    gep_lepes.append(oszlop)
    return gep_lepes

"""eredmeny = lepes()
print("A lépés:", eredmeny)"""