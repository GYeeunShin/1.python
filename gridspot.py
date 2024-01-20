import turtle
import random

wn=turtle.Screen()
wn.setup(width=200,height=200)

t=turtle.Turtle()


t.pendown()
t.speed(0)

grid=[[0,0]]


while len(grid)<25:
  
  
  rand=random.randint(0,3)
  x=t.xcor()
  y=t.ycor()

  
  if rand==0 and x<51:
    t.setheading(0)
    t.forward(50)
    x=int(round(t.xcor()))
    y=int(round(t.ycor()))
    if not([x,y] in grid):
      grid.append([x,y])
    
  if rand==1 and y<51:
    t.setheading(90)
    t.forward(50)
    x=int(round(t.xcor()))
    y=int(round(t.ycor()))
    if not([x,y] in grid):
      grid.append([x,y])
  
  if rand==2 and x>-51:
    t.setheading(180)
    t.forward(50)
    x=int(round(t.xcor()))
    y=int(round(t.ycor()))
    if not([x,y] in grid):
      grid.append([x,y])
    
  if rand ==3 and y>-51:
    t.setheading(270)
    t.forward(50)
    x=int(round(t.xcor()))
    y=int(round(t.ycor()))
    if not([x,y] in grid):
      grid.append([x,y])
  
  
  
