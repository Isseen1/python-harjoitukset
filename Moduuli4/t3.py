luku = input("Anna luku(tyhjä lopettaa):")

pienin = luku
suurin = luku

while luku != "":
    numero = int(luku)

    if pienin == luku or numero < pienin:
        pienin = numero
    if suurin is luku or numero > suurin:
        suurin = numero  
    luku = input("Anna luku (tyhjä lopettaa): ")


print("pienin luku:", pienin)
print("suurin luku:", suurin)
    


