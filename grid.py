import turtle
import random

wn=turtle.Screen()
wn.setup(width=200,height=200)

t=turtle.Turtle()

t.pendown()
t.speed(0)

grid=[[0,0]]
side=[]
forside=[[0,0]]
i=-1

while len(grid)<25:
  while len(side)<40:
      rand=random.randint(0,3)
      x=t.xcor()
      y=t.ycor()
      
    
    
      if rand==0 and x<51:
        t.setheading(0)
        t.forward(50)
        x=int(round(t.xcor()))
        y=int(round(t.ycor()))
        
        forside.append([x,y])
        i=i+1
        
        if not([x,y] in grid):
          grid.append([x,y])
          
        
      if rand==1 and y<51:
        t.setheading(90)
        t.forward(50)
        x=int(round(t.xcor()))
        y=int(round(t.ycor()))
        forside.append([x,y])
        i=i+1
        
      
        if not([x,y] in grid):
          grid.append([x,y])
          
     
      if rand==2 and x>-51:
        t.setheading(180)
        t.forward(50)
        x=int(round(t.xcor()))
        y=int(round(t.ycor()))
        forside.append([x,y])
        i=i+1
        
        if not([x,y] in grid):
          grid.append([x,y])
          
        
    
      if rand ==3 and y>-51:
        t.setheading(270)
        t.forward(50)
        x=int(round(t.xcor()))
        y=int(round(t.ycor()))
        forside.append([x,y])
        i=i+1
        
        if not([x,y] in grid):
          grid.append([x,y])
          
    
      if forside[i][0]==forside[i+1][0]:
        a=forside[i][0]
        b=int(round((forside[i][1]+forside[i+1][1])//2))
          
        if not([a,b] in side):
          side.append([a,b])
      elif forside[i][1]==forside[i+1][1]:
        a=int(round((forside[i][0]+forside[i+1][0])//2))
        b=forside[i][1]
          
        if not([a,b] in side):
          side.append([a,b])
  
    
  

    
  