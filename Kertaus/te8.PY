kustannukset = [12.5, 8.2, 15.0, 6.5, 10.8]
yhteensa = 0
for kustannus in kustannukset:
    yhteensa = yhteensa + kustannus
    print("Tuotteen valmistuskustannus: ", kustannus, "€")
    yhteensa = yhteensa + kustannus
print("Valmistuskustannusten yhteensä: ", yhteensa, "€")