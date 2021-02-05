import turtle

bob = turtle.Turtle()

bob.width(7)


#zeichnet 3 Dreiecke und ersetzt die Zahl in forward mit "laenge=50" usw.

bob.color("red")
laenge = 50
for zahl in range(3):
    bob.forward(laenge) 
    bob.left(120)

bob.color("green")
laenge_2 = 100
for zahl in range(3):
    bob.forward(laenge_2) 
    bob.left(120)

bob.color("blue")
laenge_3 = 150
for zahl in range(3):
    bob.forward(laenge_3) 
    bob.left(120)
