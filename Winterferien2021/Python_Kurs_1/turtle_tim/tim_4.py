import turtle

turtle.bgcolor("black")

tim = turtle.Turtle()
tim.goto(-200,0)
tim.shape("turtle")
tim.color("darkviolet")

tim.width(3)

#man kann auch eine bestimmte form in eine Funktion packen
#also quasi ein Bauplan, hier eine Ellipse
def ellipse():
    tim.left(45)
    for i in range(2):    
        tim.circle(100,90)
        tim.circle(100/2,90)

#hier ein viereck
def viereck():
    for j in range(4):
        tim.forward(100)
        tim.right(90)

#und hier kann man das dann ausführen
viereck()
ellipse()
viereck()
ellipse()
viereck()

