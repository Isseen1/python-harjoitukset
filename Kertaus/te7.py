sanat = ["auto","lentokone","juna","polkupyörä","laiva"]
maara = 0
for sana in sanat:
    if len(sana) > 5:
        maara = maara + 1
print("yli viisi kirjainta sisältäviä sanoja on",maara)
