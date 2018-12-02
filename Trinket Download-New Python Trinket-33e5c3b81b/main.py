#!/bin/python3

from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(15):
  write(step, align='center')
  right(90)
  for num in range(8):
    penup()
    forward(10)
    pendown()
    forward(10)
  penup()
  backward(160)
  left(90)
  forward(20)

ada = Turtle()
ada.color('dark orange')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

for turn in range(10):
  ada.right(36)

tim = Turtle()
tim.color('light blue')
tim.shape('turtle')

tim.penup()
tim.goto(-160, 70)
tim.pendown()

for turn in range(72):
  tim.left(5)

ell = Turtle()
ell.shape('turtle')
ell.color('purple')

ell.penup()
ell.goto(-160, 40)
ell.pendown()

for turn in range(60):
  ell.right(6)

jim = Turtle()
jim.shape('turtle')
jim.color('yellow')

jim.penup()
jim.goto(-160, 10)
jim.pendown()

for turn in range(30):
  jim.left(12)

for turn in range(100):
  ada.forward(randint(1,5))
  jim.forward(randint(1,5))
  tim.forward(randint(1,5))
  ell.forward(randint(1,5))
  