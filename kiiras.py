def kiiras():
    print("Tic Tac Toe Játék")
    palya = input("Válaszd ki a pálya nagyságát 3-26: ")

    while int(palya) < 3 or int(palya) > 26:
        palya = input("Válaszd ki a pálya nagyságát 3-26: ")

    meret = int(palya) 

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

    
    tabla[2][1] = 'X' 
    tabla[0][0] = 'O'
    

    print("   ", end="")
    oszlop_szam = 1
    while oszlop_szam <= meret:
        print(f" {oszlop_szam:<2} ", end="") 
        oszlop_szam = oszlop_szam + 1
    print()

    print("  " + "────" * meret) 

    sor_index = 0
    while sor_index < meret:
        print(chr(65 + sor_index), end=" ")
        
        oszlop_index = 0
        while oszlop_index < meret:
            print(f"│ {tabla[sor_index][oszlop_index]} ", end="")
            oszlop_index = oszlop_index + 1
        
        print("│") 
        
        print("  " + "────" * meret)
        
        sor_index = sor_index + 1
