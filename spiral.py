import math
import turtle

def spiral(n):
    """draws a square spircal with n number of lines"""

    for x in range(n):
        turtle.forward(x*5)
        turtle.left(90)
        turtle.forward(x*5)

    turtle.exitonclick()
