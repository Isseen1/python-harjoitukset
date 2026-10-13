oikea_tunnus = "metropolia"
oikea_salasana = "opiskelija1"
yritykset = 0

while yritykset < 5:
    tunnus = input("Anna käyttäjätunnus:")
    salasana = input("Anna salasana: ")
    yritykset = yritykset + 1
    if tunnus == oikea_tunnus and salasana == oikea_salasana:
       print("Tervetuloa")
       break
    else:
        print("Väärä tunnus tai salasana")
        yritykset += 1
if yritykset == 5:
    print("Pääsy evätty!")       


