
preis = 25


print("preis =", preis)

bezahlt = int(input("Ich bezahle:"))

#print("ich bezahle", bezahlt)

#print(preis < bezahlt)

if preis < bezahlt:
    print("danke, reicht. Wechselgeld=",bezahlt-preis,"€")

else:
    print("geld reicht nicht!")
