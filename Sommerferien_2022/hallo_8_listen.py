
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
if bl == "0":
    print(">>>>", bundeslandliste[0])

