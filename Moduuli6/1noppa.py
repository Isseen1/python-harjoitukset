import random
def heita_noppaa():
    return random.randint(1, 6)
luku = 0
while luku != 6:
    luku = heita_noppaa()
    print(luku)