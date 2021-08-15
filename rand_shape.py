import turtle
import random
colorarray=["yellow","gold","orange","red","maroon","violet","magenta","purple","navy","blue", 
            "skyblue", "cyan", "turquoise", "lightgreen", "green",
            "darkgreen", "chocolate", "brown", "black", "gray",]
turtle.speed(0)
def rectangle (size):
    lengrand=random.randint(1,2)
    breadrand=random.randint(1,2)
    if lengrand==1:
        leng=size*1/3*2
    else:
        leng=size*2/3*2
    if breadrand==1:
        bread=size*1/4*2
    else:
        bread=size*2/4*2
    for rect in range(2):
        turtle.forward(leng)
        turtle.right(90)
        turtle.forward(bread)
        turtle.right(90)
def parallelogram (size):
    parlengrand=random.randint(1,2)
    parbreadrand=random.randint(1,2)
    if parlengrand==1:
        leng=size*1/3*4
    else:
        leng=size*2/3*4
    if parbreadrand==1:
        bread=size*1/4*4
    else:
        bread=size*2/4*4
    while True:
        parangle1=random.randint(30,130)
        parangle2=random.randint(30,130)
        if parangle1+parangle2==180:
            break
    for rect in range(2):
        turtle.forward(leng)
        turtle.right(parangle1)
        turtle.forward(bread)
        turtle.right(parangle2)
def circle (size):
    turtle.circle(size/2)
def polygon (size,sides):
    for penta in range(sides):
        turtle.forward(size*sides/(sides+1))
        turtle.right(360/sides)
        

for yeet in range (100):
    x=random.randint(-655,655)
    y=random.randint(-345,345)
    width=random.randint(1,6)
    size=random.randint(10,75)
    color=random.choice(colorarray)
    turtle.color(color)
    turtle.penup()
    turtle.width(width)
    turtle.goto(x,y)
    turtle.pendown()
    fillind=random.randint(1,2)
    if fillind==1:
        turtle.begin_fill()
    
    shape=random.randint(0,13)
    if shape==1 :
        rectangle(size)
    if shape==2:
        circle(size)
    if shape==0:
        parallelogram(size)
    if shape>2:
        polygon(size,shape)
    if fillind==1:
        turtle.end_fill()
randomvar=input("this is for keeping the turtle graphics window open so pls dont type anyhting")