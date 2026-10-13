ostoslista = ["maito", "leipä", "omenat", "juusto"]

while ostoslista:
    
    tuote = input("Minkä tuotteen ostit? ").lower()

    if tuote in ostoslista:
        ostoslista.remove(tuote)
        print("Jäljellä olevat tuotteet:", ostoslista)
    else:
        print("Tuotetta ei ole ostoslistalla.")

print("Kaikki tuotteet on ostettu!")