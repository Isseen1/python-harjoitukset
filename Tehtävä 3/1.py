pituus = float(input("Anna kuhan pituus senttimetreinä: ")) 

if pituus <37:
    puuttu = 37 - pituus
    print("laske kuha takaisin järveen")
    print("alimman pituus on 37 cm, puuttuu vielä" , puuttu, "cm")
else:
    print("kuha on riittävän pitkä")


