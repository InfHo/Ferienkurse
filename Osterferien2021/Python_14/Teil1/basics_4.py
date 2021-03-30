
test_liste = ["Zitrone", "Apfel", "Fleisch", "Orange", "Eistee", "Kiwi"]


for i in range(5):
    print(i, i*100)

print(10*"-")

for j in test_liste:
    print(j)

print(10*"-")

for k in [11,2,14,9]:
    print(k)

print(10*"-")

x = 0

for l in range(10):
    print(l,")", "x=", x)
    x = x + 1

hello = "Hello "
var_input = input("Gib etwas ein:")

print(hello + var_input)
