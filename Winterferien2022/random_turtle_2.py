import turtle
import random

turtle.colormode(255)

fred = turtle.Turtle()

fred.shape("turtle")

fred.speed(0)
fred.width(5)

##for i in range(100):
while True:    
##    r = random.randint(200,255)
##    g = random.randint(0,255)
##    b = random.randint(100,200)
##    
##    fred.color([r,g,b])
##    
##    fred.forward(random.randint(15,25))
    fred.color(random.choice(["red","green","blue"]))
    fred.forward(25)

    fred.right(random.choice([90,270]))

##    if random.randint(0,10) == 5:
##        fred.circle(50)
