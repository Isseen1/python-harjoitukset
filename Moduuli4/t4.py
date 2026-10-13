import random
luku = random.randint(1, 10)
arvaus = int(input("Arvaa luku väliltä 1-10: "))
while arvaus != luku:
    if arvaus > luku:
        print("liian suuri arvaus")
    else:
        print("lian pieni arvaus")
    arvaus = int(input("Arvaa luku väliltä 1-10:"))

   
    print("oikein Arvattu")       

