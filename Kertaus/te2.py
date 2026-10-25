luku = int(input("Anna kokonaisluku:"))
if luku % 3 == 0 and luku % 5 == 0:
    print("jaollinen molemilla luvuilla!")   
elif luku % 3 == 0:
    print("Kolmella jaollinen")
elif luku % 5 == 0:
    print("Viidellä jaollinen")
else:
    print("luku ei ole jaollinen kolmella eikä viidellä")
                