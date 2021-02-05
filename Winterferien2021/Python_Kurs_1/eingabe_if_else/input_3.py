
preis = 23.75

print("Der Preis ist:", preis)

bezahlt = input("ich bezahle in bar: ")

print(bezahlt)

#problem: bezahlt und preis sind unterschiedliche datentypen
print(type(preis))
print(type(bezahlt))

#das heisst man kann sie zb nicht addieren
print(preis+bezahlt)
