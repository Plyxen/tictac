def palya_meret():
    print("Tic Tac Toe Játék")
    palya = input("Válaszd ki a pálya nagyságát 3-26: ")

    while int(palya) < 3 or int(palya) > 26:
        palya = input("Válaszd ki a pálya nagyságát 3-26: ")
        
    meret = int(palya) 
    return meret

def palya(meret,tabla):
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