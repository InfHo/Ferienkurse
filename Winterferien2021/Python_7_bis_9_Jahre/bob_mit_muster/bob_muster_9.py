import turtle

bob = turtle.Turtle()

bob.width(7)

def dreiecksmuster(laenge,farbe):
	bob.color(farbe)
	for zahl in range(3):
	    bob.forward(laenge) 
	    bob.left(120)

#man kann die Bezeichnung mit '=' in den Klammern auch weglassen.
#Wichtig ist nur die Reihenfolge
dreiecksmuster(50, "red")
dreiecksmuster(100, "green")
dreiecksmuster(150, "blue")
