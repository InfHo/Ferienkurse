
def additionsrechner(a,b):
    print(a+b)


x = input("gib etwas ein: ")

if x == "Hallo":
    print("wie gehts")

if x == "t":
    print("du hast auf 't' gedrückt...")

if x == "rechner":
    a = int(input("zahl 1:"))
    b = int(input("zahl 2:"))
    additionsrechner(a,b)
else:
    print("irgend was anderes")
