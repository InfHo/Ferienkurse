
test_liste = ["Zitrone", "Apfel", "Fleisch", "Orange", "Eistee", "Kiwi"]

test_liste.append("Brot_c")

z = len(test_liste)
print(test_liste, z)

print("type(z):", type(z))

print(test_liste[0])

for i in range(len(test_liste)):
    print(i, ">>>", test_liste[i])
