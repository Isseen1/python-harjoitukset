import random
oikea_luku = random.randint(1, 10)
arvaus = int(input("Arvaa luku väliltä 1-10: "))
while arvaus != oikea_luku:
    if arvaus > oikea_luku:
        print("liian suuri arvaus")
    else:
        print("lian pieni arvaus")
    arvaus = int(input("arvaa uudelleen:"))
   
    print("oikein")       

