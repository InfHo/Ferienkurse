import turtle

turtle.bgcolor("black")

tim = turtle.Turtle()
tim.shape("turtle")
tim.color("darkviolet")

tim.width(9)

zahl_1 = 50
zahl_winkel_1 = 40

#man kann auch durch Farben loopen
for farbe in ("darkkhaki", "orchid", "cyan","tomato", "lawngreen"):
    tim.color(farbe)
    tim.forward(zahl_1)
    tim.left(zahl_winkel_1)

tim.color("green")
