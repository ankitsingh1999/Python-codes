#first project
#"circle of squares"

import turtle
ank_turtle = turtle.Turtle()
#speed() is used to speed up the code
ank_turtle.speed(0)

def cos(length,angle):
    for i in range(4):
        ank_turtle.forward(length)
        ank_turtle.right(angle)
        
#make a square turn 11 degree, again make a square and on loop... 
for i in range(100):
#it will make a square 
    cos(100,90)
#turn 11 degree 
    ank_turtle.right(11)
    





        

