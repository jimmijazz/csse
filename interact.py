import turtle
import math

def interact():
    distance = input("Please enter your distance: ")
    direction_list = {'n':90,'s':270,'e':0,'w':180}
    turtle.reset()
    
    while True:
        direction = input('Which direction? :')
        if direction == 'q':
            turtle.exitonclick()
            break
        elif direction in direction_list:         
            turtle.setheading(direction_list[direction])
            turtle.forward(float(distance))
        else:
            print('That is not  a direction')
