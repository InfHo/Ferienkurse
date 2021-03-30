
test_liste = ["Zitrone", "Apfel", "Fleisch", "Orange", "Eistee", "Kiwi"]

for i in range(len(test_liste)):
    print(i+1, test_liste[i])

print("------")

var_input = int(input("Enter number:"))

if var_input <= len(test_liste):
    print(test_liste[var_input-1])

else:
    print("Number out of range")


def saetze_basteln(wort_1, wort_2):
    print(wort_1+" "+wort_2)

saetze_basteln("Hello","how is it going?")

saetze_basteln("tja","was soll ich sagen?")

saetze_basteln("afafeafv", "afdafji jpij padwa?")





def additions_rechner(x,y,z, q):
    
    print(x+y+z)
    print(q)

additions_rechner(1,2,3, "Hallo")

additions_rechner(10,5,5, "aaa")

