
preis = 23.75

print("Der Preis ist:", preis)

bezahlt = float(input("ich bezahle in bar: "))



print("Ich habe bezahlt:", bezahlt)

# if = "falls" 
if bezahlt < preis:
    print("das Geld reicht nicht. Es fehlen noch:", preis-bezahlt, "€")

#elif = else if = "oder falls sonst das passiert"
elif bezahlt > preis:
    print("Sie haben zuviel bezahlt. Das wären ", bezahlt-preis, "€ Trinkgeld.")

#ganz am Ende und soll nur 1x vorkommen: else= "oder sonst"
else:
    print("Sie haben genau richtig bezahlt. 🍔🍟")
