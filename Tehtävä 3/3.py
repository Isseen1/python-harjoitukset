 
sukupuoli =input("Anna biologinen sukupuoli (mies/nainen): ")

hemoglobiini = float(input("Anna hemoglobiiniarvo (g/l): "))
if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiini <= 175:
        print("hemoglobiiniarvo on normaali.")
    else:
        print("hemoglobiiniarvo on korkea.")

elif sukupuoli == "mies":
    if hemoglobiini < 134:
        print("hemoglobiiniarvo on alhainen.")
    elif hemoglobiini <= 195:
        print("hemoglobiiniarvo on normaali.")
    else:
        print("hemoglobiiniarvo on korkea.")
