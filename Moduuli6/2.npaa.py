import random
def heita_noppaa(tahkot):
    return random.randint(1, tahkot)
tahkot = int(input("Anna nopan tahkojen määrä: "))
luku = 0
while luku != tahkot:
    luku = heita_noppaa(tahkot)
    print(luku)