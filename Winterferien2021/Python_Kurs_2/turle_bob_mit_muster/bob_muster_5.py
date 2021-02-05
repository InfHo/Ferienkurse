import turtle

bob = turtle.Turtle()

bob.width(7)


#setzt die dreiecke in funktionen "def" ('Bauplan')

def dreiecksmuster_1():
	bob.color("red")
	laenge = 50
	for zahl in range(3):
	    bob.forward(laenge) 
	    bob.left(120)

def dreiecksmuster_2():
	bob.color("green")
	laenge_2 = 100
	for zahl in range(3):
	    bob.forward(laenge_2) 
	    bob.left(120)

def dreiecksmuster_3():
	bob.color("blue")
	laenge_3 = 150
	for zahl in range(3):
	    bob.forward(laenge_3) 
	    bob.left(120)

#und hier werden die Baupläne dann ausgeführt
dreiecksmuster_1()
dreiecksmuster_2()
dreiecksmuster_3()
