import turtle
import random

turtle.colormode(255)

fred = turtle.Turtle()

fred.shape("turtle")

fred.speed(0)
fred.width(3)

##for i in range(100):
while True:    
    r = random.randint(0,255)
    g = random.randint(50,100)
    b = random.randint(200,250)
    
    fred.color([r,g,b])
    
    fred.forward(random.randint(5,20))

    fred.right(random.randint(0,180))
