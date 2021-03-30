
test_liste = ["Zitrone", "Apfel", "Fleisch", "Orange", "Eistee", "Kiwi"]

for i in range(len(test_liste)):
    print(i+1, test_liste[i])

print("------")

var_input = int(input("Enter number:"))

if var_input <= len(test_liste):
    print(test_liste[var_input-1])

else:
    print("Number out of range")
