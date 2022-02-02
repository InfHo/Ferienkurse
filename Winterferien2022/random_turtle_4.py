import turtle
import random

turtle.colormode(255)

fred = turtle.Turtle()

fred.shape("turtle")

fred.speed(0)
fred.width(5)
r = 0

while True:    
##    r = random.randint(200,255)
##    g = random.randint(0,255)
##    b = random.randint(100,200)
    if r < 255:
        r = r + 1
    
    if r == 255:
        r = 0
    
    g = 255-r
    b = 100
    fred.color([r,g,b])
        
    fred.forward(25)
    fred.right(random.choice([90,270]))

    if r % 50 == 0:
        fred.write("Hallo", font=("Verdana", 20))

    print("r:",r)
