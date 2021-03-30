import turtle
import random

turtle.colormode(255)

tim = turtle.Turtle()


tim.speed(200)


def ellipse(schnitzel,remoulade):
        tim.begin_fill()
        tim.color(remoulade)
        tim.left(45)
        for i in range(2):    
                tim.circle(schnitzel,90)
                tim.circle(schnitzel/2,90)
        tim.end_fill()
        tim.right(45)
        


for i in range(100):
    
    farbe = random.randint(0,255), random.randint(0,200), random.randint(0,255)
    ellipse(random.randint(25,75),farbe)
    tim.pu()
    tim.goto(random.randint(-450,450),random.randint(-400,400))
    tim.pd()
    print(i)

