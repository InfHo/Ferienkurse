
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
neues_bl = input("Gib ein fehlendes Bundesland ein:")
bundeslandliste.append(neues_bl)
print(bundeslandliste)

print(">>>>", bundeslandliste[1])
