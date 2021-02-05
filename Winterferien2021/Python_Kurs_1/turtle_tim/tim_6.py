import turtle

turtle.bgcolor("black")

tim = turtle.Turtle()
tim.goto(-200,0)
tim.shape("turtle")
tim.color("darkviolet")

tim.width(3)


#die laengen werden jetzt durch variablen ersetzt
def viereck():
    laenge = 50
    tim.color("darkviolet")
    for j in range(4):
        tim.forward(laenge)
        tim.right(90)

def viereck_2():
    laenge = 150
    tim.color("light blue")
    for j in range(4):
        tim.forward(laenge)
        tim.right(90)

def viereck_3():
    laenge = 250
    tim.color("yellow")
    for j in range(4):
        tim.forward(laenge)
        tim.right(90)

viereck()
viereck_2()
viereck_3()
