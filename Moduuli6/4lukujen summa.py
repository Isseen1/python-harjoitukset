def laske_summa(luvut):
    summa = 0
    for luku in luvut:
        summa = summa + luku
    return summa
lista = [2, 4, 6, 8]
tulos = laske_summa(lista)
print("Summa on:", tulos)
