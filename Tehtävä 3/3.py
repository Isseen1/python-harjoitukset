 
sukupuoli =input("Anna biologinen sukupuoli (mies/nainen): ")

hemoglobiini = int(input("Anna hemoglobiiniarvo (g/l): "))
if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiini >= 175:
        print("hemoglobiiniarvo on korkea.")
    else:
        print("hemoglobiiniarvo on normaali.")

elif sukupuoli == "mies":
    if hemoglobiini < 134:
        print("hemoglobiiniarvo on alhainen.")
    elif hemoglobiini >= 195:
        print("hemoglobiiniarvo on korkea.")
    else:
        print("hemoglobiiniarvo on normaali.")
