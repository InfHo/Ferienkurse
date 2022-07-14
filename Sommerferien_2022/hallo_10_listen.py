
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


def plan_a():
    bl = input("gib eine Zahl ein")

    c = int(bl)

    if c < len(bundeslandliste):
        print(">>>>", bundeslandliste[c])

    else:
        print("Du hast falsch ausgewählt. Versuche es noch einmal!")
        plan_a()
        
plan_a()
