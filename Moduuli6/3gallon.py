def muuta_litroiksi(gallonat):
    return gallonat * 3.785
gallonat = float(input("Anna gallonamäärä: "))
while gallonat >= 0:
    litrat = muuta_litroiksi(gallonat)
    print("litroina:",litrat)
    gallonat = float(input("Anna gallonamäärä: "))