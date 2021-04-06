#making a square using multiple arguments!

import turtle

ankit_turtle = turtle.Turtle()
def square(length,angle):
    
    
    ankit_turtle.forward(length)
    ankit_turtle.right(angle)
    ankit_turtle.forward(length)
    ankit_turtle.right(angle)
    ankit_turtle.forward(length)
    ankit_turtle.right(angle)
    ankit_turtle.forward(length)


square(200,90)
square(200,90)
square(200,90)
square(200,90)


