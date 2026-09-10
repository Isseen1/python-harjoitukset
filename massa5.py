leiviskat = float(input("Anna leiviskät: "))

naulat = float(input("Anna naulat: "))

luodit = float(input("Anna luodit: "))

grammat = (leiviskat *20 * 32 * 13.3) + (naulat * 32 * 13.3) + (luodit * 13.3)

kilogrammat = int(grammat / 1000)

jaljelle_jaavat_grammat = grammat % 1000

print(f"massa on {kilogrammat} kilogrammaa ja {jaljelle_jaavat_grammat:.2f} grammaa")


