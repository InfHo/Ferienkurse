import turtle

turtle.bgcolor("black")

tim = turtle.Turtle()

#hier kann man den startpunk eingeben
tim.goto(50,50)

tim.shape("turtle")
tim.color("darkviolet")

tim.width(3)

#da die Funktionen gleich aussehen braucht man also eigentlich nur eine
#und man kann die Farben auch gleich als Variable ersetzen
def viereck(laenge, farbe):
    tim.color(farbe)
    for j in range(4):
        tim.forward(laenge)
        tim.right(90)

#und am Ende noch dasselbe mit der Ellipse vom Anfang
def ellipse(schnitzel,remoulade):
        tim.color(remoulade)
        tim.left(45)
        for i in range(2):    
                tim.circle(schnitzel,90)
                tim.circle(schnitzel/2,90)
        tim.right(45)


viereck(50, "yellow")
viereck(150, "green")
viereck(250, "red")


ellipse(50,"yellow")
ellipse(150, "blue")
ellipse(250, "orange")
