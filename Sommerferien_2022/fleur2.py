from turtle import *
speed(0)
colormode(255)
bgcolor("black")
def fleur():
    for i in range(300):
        circle(190-i,90)
        left(90)
        circle(190-i,90)
        left(18)
        color([i%10,50,i%255])
        print(i%255)
fleur()
