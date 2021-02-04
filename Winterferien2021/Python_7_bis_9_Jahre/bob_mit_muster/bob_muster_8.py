import turtle

bob = turtle.Turtle()

bob.width(7)

#dasselbe wie mit laneg geht auch mit Farbe, und vielem mehr!
def dreiecksmuster(laenge,farbe):
	bob.color(farbe)
	for zahl in range(3):
	    bob.forward(laenge) 
	    bob.left(120)

#hier kann man jetzt die Farbe selbst verändern
dreiecksmuster(laenge = 50, farbe="red")
dreiecksmuster(laenge = 100, farbe="green")
dreiecksmuster(laenge = 150, farbe="blue")
