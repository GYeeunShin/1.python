import turtle
import random
import time

def drawScreenBorders():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(-350,350)
    pen.pendown()
    for i in range(4):
        pen.forward(700)
        pen.right(90)

def initializeTheCells():
    for i in range(35):
        cells.append([])
        for j in range(35):
            newCell = turtle.Turtle()
            newCell.penup()
            newCell.shape("square")
            newCell.shapesize(stretch_wid = 0.9, stretch_len = 0.9)
            cells[i].append(newCell)
            rand = random.randint(0, 1)
            newCell.state = rand
            if rand == 0:
                newCell.color("gray100") 
            else: 
                newCell.color("gray0")

                      
def showTheUniverse(): 
    ycor = 340
    for i in range(35):
        xcor = -340
        for j in range(35):
            cells[i][j].goto(xcor, ycor)
            xcor += 20
        ycor -= 20
        

def esc():
    global stop
    stop = True

def getNeighbors(i, j):
    total = 0
    for a in [-1,0,1]:
        for b in [-1,0,1]:
            if a==0 and b == 0:
                continue 
            if boundaryCondition == 1:
                if 0<i+a<35 and 0<j+b<35:
                    total = total + cells[i+a][j+b].state
                    
            elif boundaryCondition == 2:
                total = total + cells[(i+a) % 35][(j+b) % 35].state
                
    return total
    
        


def updateCells():
    
    updated_cells= [[0] * 35 for j in range(35)]
    for i in range(35):
        for j in range(35):
            total=getNeighbors(i, j) 
            if cells[i][j].state==1:
                if total <2 or total >3:
                    updated_cells[i][j]=0
                else:
                    updated_cells[i][j]=1
            else:
                if total==3:
                    updated_cells[i][j]=1
                    
    for i in range(35):
        for j in range(35):
            cells[i][j].state=updated_cells[i][j]
            if cells[i][j].state==0:
                cells[i][j].color("gray100")
            else:
                cells[i][j].color("gray0")

    return cells

    
   


boundaryCondition = int(input("Choose the Boundary Condition? \nEnter 1 for Constant or 2 for Periodic: "))
print("Press ESC to exit")

wn = turtle.Screen()
wn.setup(width = 35*20, height = 35*20)
wn.title("Life Game")
wn.tracer(0)

wn.listen()
wn.onkeypress(esc, "Escape") 


stop = False 
cells = []

drawScreenBorders() 
initializeTheCells() 
showTheUniverse() 


while not stop:
    wn.update()
    updateCells()
    time.sleep(0.05)

