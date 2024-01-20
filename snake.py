import turtle
import random
import time

wn=turtle.Screen()
wn.tracer(0)
wn.setup(width=600,height=600)
head=turtle.Turtle()

head.shape("square")
head.penup()
head.speed(1)
head.color("pink")


direction="r"

obs=[]

food=turtle.Turtle()
food.shape("square")
food.penup()
food.speed(1)
food.color("pale turquoise")
x=random.randint(-14,14)
y=random.randint(-14,14)
food.goto(x*20,y*20)

count1=0
while count1<9:
  
  obs1=turtle.Turtle()
  obs1.shape("square")
  obs1.penup()
  obs1.speed(1)
  obs1.color("coral")
  x1=random.randint(-14,14)
  y1=random.randint(-14,14)
  obs1.goto(x1*20,y1*20)
  obs.append(obs1)

  if obs[count1].xcor()==obs[count1-1].xcor() and obs[count1].ycor()==obs[count1 - 1].ycor():
        x=random.randint(-14,14)
        y=random.randint(-14,14)
        obs1.goto(x*20,y*20)
  else:
    count1+=1

  
def moveUp():
  global direction
  if direction != "d":
      direction = "u"
def moveDown():
  global direction
  if direction != "u":
    direction = "d"
def moveRight():
  global direction
  if direction != "l":
    direction = "r"

def moveLeft():
  global direction
  if direction != "r":
    direction = "l"
    
wn.listen() 
wn.onkeypress(moveUp,"Up")
wn.onkeypress(moveDown,"Down")
wn.onkeypress(moveLeft,"Left")
wn.onkeypress(moveRight,"Right")

snake=[]
snake.append(head)
count=1



    
while count<4:
  newTail=turtle.Turtle()
  newTail.shape("square")
  newTail.speed(1)
  newTail.color("pink")
  newTail.penup()
  newTail.goto(count*(-20),0)
  snake.append(newTail)
  count+=1


game_on=True
while game_on:
    
    time.sleep(0.1)
    
    i=len(snake)-1
    
    while i>0:
      snake[i].goto(snake[i-1].xcor(),snake[i-1].ycor())
      i=i-1
      
    
    
    wn.update()
    
    if direction=="u":
      head.sety(head.ycor()+20)
    elif direction == "d":
      head.sety(head.ycor()-20)
    elif direction == "r":
      head.setx(head.xcor()+20)
    elif direction == "l":
      head.setx(head.xcor()-20)

    if head.xcor()>300:
      head.setx(-300)
    elif head.xcor()<-300:
      head.setx(300)
    elif head.ycor()>300:
      head.sety(-300)
    elif head.ycor()<-300:
      head.sety(300)
    
    if abs(head.xcor()-food.xcor())<2 and abs(head.ycor()-food.ycor())<2:
      newTail=turtle.Turtle()
      newTail.shape("square")
      newTail.speed(1)
      newTail.penup()
      newTail.color("pink")
      snake.append(newTail)
      x=random.randint(-14,14)
      y=random.randint(-14,14)
      food.goto(x*20,y*20)

    
    p=0
    while p<10:
      if abs(head.xcor()-obs[p].xcor())<2 and abs(head.ycor()-obs[p].ycor())<2:
        game_on = False
      else:
        p=p+1
      
      
    for newTail in snake:
      if newTail.distance(head)<2:
        break
    
    k=len(snake)-1
    while k>-1:
      
      if snake[k].xcor()==food.xcor() and snake[k].ycor()==food.ycor():
        x=random.randint(-14,14)
        y=random.randint(-14,14)
        food.goto(x*20,y*20)
        k=len(snake)-1
        
      else:
        k=k-1
    
    

      

    

    

   

 
    




