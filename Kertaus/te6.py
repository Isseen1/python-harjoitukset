arvot = []
while True:
    arvo = int(input("Anna arvo: "))
    if arvo == 0:
        break

    arvot.append(arvo)

    print("lisäysjärjestyksessä:", arvot)

    jarjestys =arvot[:]
    jarjestys.sort()
    print("Pienimmästä suurimpaan:",jarjestys)
