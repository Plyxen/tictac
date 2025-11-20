current = 1
palya = 0
szamok = 1

print("Tic Tac Toe Játék")
palya = input("Válaszd ki a pálya nagyságát 3-100: ")
while int(palya) < 3 or int(palya) > 100:
    palya = input("Válaszd ki a pálya nagyságát 3-100: ")
    
szamok = palya

while int(current) <= int(szamok):
    print(current, end=' ') 
    current = current + 1

