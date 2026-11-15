import turtle
import time

t = turtle.Turtle()

screen = turtle.Screen() #creo una tortuga
screen.setup(width=800, height=600)
t.speed(1) #velocida lenta
t.color('red') # color

time.sleep(2)

for _ in range(4):
    t.forward(100)
    t.right(90)


turtle.done()