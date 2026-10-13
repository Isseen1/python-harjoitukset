pituus = float(input("Anna kuhan pituus (cm): "))

if pituus < 37:
    puuttuu = 37 - pituus
    print("Laske kuha takaisin järveen.")
    print("Pituudesta puuttuu", puuttuu, "cm.")