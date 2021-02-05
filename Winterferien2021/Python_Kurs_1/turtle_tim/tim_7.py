import turtle

turtle.bgcolor("black")

tim = turtle.Turtle()
tim.goto(-200,0)
tim.shape("turtle")
tim.color("darkviolet")

tim.width(3)


#die laenge kann man auch in die Klammern einfügen
#und unten dann beim ausführen eingeben
#wenn man genau hinschaut sieht man auch das die 3 Baupläne eigentlich fast
#gleich aussehen...
def viereck(laenge):
    tim.color("darkviolet")
    for j in range(4):
        tim.forward(laenge)
        tim.right(90)

def viereck_2(laenge):
    tim.color("light blue")
    for j in range(4):
        tim.forward(laenge)
        tim.right(90)

def viereck_3(laenge):
    tim.color("yellow")
    for j in range(4):
        tim.forward(laenge)
        tim.right(90)

#jetzt kann man die Funktionen, also die Baupläne ausführen
#und Längen eingeben wie man möchte ohne jedesmal den kompletten Plan
#ändern zu müssen
viereck(laenge = 50)
viereck_2(laenge = 150)
viereck_3(laenge = 250)
