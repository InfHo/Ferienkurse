import turtle

bob = turtle.Turtle()

bob.width(7)

#weil die laenge jetzt überall erstzt wurde kann man
#auch nur eine Funktion benutzen ......
def dreiecksmuster(laenge):
	bob.color("red")
	for zahl in range(3):
	    bob.forward(laenge) 
	    bob.left(120)
	    
#.....und dort die verschiedene Länge je nach Wunsch eingeben
dreiecksmuster(laenge = 50)
dreiecksmuster(laenge = 100)
dreiecksmuster(laenge = 150)
