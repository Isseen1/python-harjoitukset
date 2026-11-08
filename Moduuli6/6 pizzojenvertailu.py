import math
def yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 200
    pinta_ala = math.pi *sade **2
    return hinta / pinta_ala
halkaisija1 = float(input("Anna pizzan 1 halkaisija: "))
hinta1 =float(input("Anna pizzan 1 hinta: "))
halkaisija2 = float(input("Anna pizzan 2 halkaisija: "))
hinta2 = float(input("Anna pizzan 2 hinta: "))
yksikkohinta1 = yksikkohinta(halkaisija1, hinta1)
yksikkohinta2 = yksikkohinta(halkaisija2, hinta2)
if yksikkohinta1 < yksikkohinta2:
    print("Pizza 1 antaa paremman vastineen rahalle")
elif yksikkohinta2 < yksikkohinta1:
    print("Pizza 2 antaa paremman vastineen rahalle")
else:
    print("Pizzat ovat yhtä edullisia")
