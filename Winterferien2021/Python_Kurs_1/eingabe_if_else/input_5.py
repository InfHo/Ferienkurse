
preis = 23.75

print("Der Preis ist:", preis)

bezahlt = float(input("ich bezahle in bar: "))

print("Ich habe bezahlt:", bezahlt)

#jetzt kann man schauen ob bezahlt kleiner als der Preis ist
if bezahlt < preis:
    print("das Geld reicht nicht. Es fehlen noch:", preis-bezahlt, "€")

