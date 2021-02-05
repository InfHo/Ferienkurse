import turtle

bob = turtle.Turtle()

bob.shape("turtle")

bob.speed(20)

bob.width(7)
bob.forward(50) 


#pu = pen up, damit kann man strecken überspringen ohne 
#zu zeichnen
bob.pu()
bob.forward(50) 

#und mit pd wieder weiterzeichnen
bob.pd()
bob.forward(50)
