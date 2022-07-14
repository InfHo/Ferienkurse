
bundeslandliste = ["NRW",
                   "BW",
                   "Berlin",
                   "Niedersachsen",
                   "Thüringen",
                   "Saarland",
                   "Rheinland Pfalz",
                   "Bayern",
                   "Sachsen",
                   "Sachsen-Anhalt",
                   "Bremen",
                   "Hamburg",
                   "Schleswig-Holstein"]


bundeslandliste.append("Mecklenburg-Vorpommern")

print(len(bundeslandliste))
print(bundeslandliste)


bl = input("gib eine Zahl ein")

c = int(bl)
##print(bl, type(bl))


if c < len(bundeslandliste):
    print(">>>>", bundeslandliste[c])

else:
    print("Zahl ausserhalb der Liste")

