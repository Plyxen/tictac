import kiiras
import lepes

def tabla(meret):
    tabla = [] 
    tabla_sor_index = 0
    while tabla_sor_index < meret:
        tabla_oszlop_index = 0
        aktualis_sor = [] 
        while tabla_oszlop_index < meret:
            aktualis_sor.append(' ') 
            tabla_oszlop_index = tabla_oszlop_index + 1
        tabla.append(aktualis_sor)
        tabla_sor_index = tabla_sor_index + 1

    return tabla
    
meret=kiiras.palya_meret()
jatekos_tabla=tabla(meret)
kiiras.palya(meret, jatekos_tabla)
lepes.lepes(meret, jatekos_tabla)
lepes.jatekos_lepes(meret, jatekos_tabla)