
import math
import random
import numpy as np

# (x,y) Dot coordinate
# (Cx,Cy) Cicle centre coordinate)


def isPointInCircle(x, y, Cx, Cy, r=1):
    return math.sqrt((x - Cx)**2 + (y - Cy)**2) <= r
                    
def approximateCircleArea(r, numberOfPoints):
    squareSide = r*2
    Cx = r
    Cy = r

    #print(Cx)
    #print(Cy)
    #print(squareSide)

    pointsInside = 0
    i=0
    while i <= numberOfPoints:
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        print(x,y)
        #print(y)
    #    print(numberOfPoints)
        i+=1
        d = math.sqrt((x - 0)**2 + (y - 0)**2)
       # print(d)
    
       # if (isPointInCircle(x, y, Cx, Cy, r)):
        if d <=1:
            pointsInside +=1
    print("Number of points inside the circle = ", pointsInside)
            #print("Square Side = ", squareSide)
            #print("numberOfPoints = ", numberOfPoints)
    print("Circle Area = ", (pointsInside / numberOfPoints) * squareSide**2)
    return pointsInside / numberOfPoints * squareSide**2
    

approximateCircleArea(1,10000.0)

#print(x)
#print(y)
#print(pointsInside / numberOfPoints * squareSide**2)
    
