import turtle

bob = turtle.Turtle()

bob.width(7)

#setze laenge in Klammern in den Bauplan. dann kann man die Länge unten 
#direkt eingeben in der Grösse wie man möchte

def dreiecksmuster_1(laenge):
	bob.color("red")
	for zahl in range(3):
	    bob.forward(laenge) 
	    bob.left(120)

def dreiecksmuster_2(laenge_2):
	bob.color("green")
	for zahl in range(3):
	    bob.forward(laenge_2) 
	    bob.left(120)

def dreiecksmuster_3(laenge_3):
	bob.color("blue")
	for zahl in range(3):
	    bob.forward(laenge_3) 
	    bob.left(120)

dreiecksmuster_1(laenge = 50)
dreiecksmuster_2(laenge_2 = 100)
dreiecksmuster_3(laenge_3 = 150)
