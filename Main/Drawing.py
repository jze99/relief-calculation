from turtle import *
import sys
import json
import math
import Point

receivedReferenceValues = json.loads(sys.argv[1])# массив с данными

size = 100

Vector2 = [
    [[-size*3,size*3],
     [-size*2,size*3],
     [-size,size*3],
     [0,size*3],
     [size,size*3],
     [size*2,size*3],
     [size*3,size*3]
     ],
    [[-size*3,size*2],
     [-size*2,size*2],
     [-size,size*2],
     [0,size*2],
     [size,size*2],
     [size*2,size*2],
     [size*3,size*2]
     ],
    [[-size*3,size],
     [-size*2,size],
     [-size,size],
     [0,size],
     [size,size],
     [size*2,size],
     [size*3,size]
     ],
    [[-size*3,0],
     [-size*2,0],[-size,0],
     [0,0],[size,0],
     [size*2,0],
     [size*3,0]
     ],
    [[-size*3,-size],
     [-size*2,-size],
     [-size,-size],
     [0,-size],
     [size,-size],
     [size*2,-size],
     [size*3,-size]
     ],
    [[-size*3,-size*2],
     [-size*2,-size*2],
     [-size,-size*2],
     [0,-size*2],
     [size,-size*2],
     [size*2,-size*2],
     [size*3,-size*2]
     ],
    [[-size*3,-size*3],
     [-size*2,-size*3],
     [-size,-size*3],
     [0,-size*3],
     [size,-size*3],
     [size*2,-size*3],
     [size*3,-size*3]
     ]
    ]

horizontalBots = []
verticalBots = []

def CreatingPoints():
    for i in range(len(Vector2)):
        for j in range(len(Vector2[i])):
            horizontalBots.append(Point.point(X = Vector2[i][j][0], Y = Vector2[i][j][1], Height = round(receivedReferenceValues[i][j], 1)))
            verticalBots.append(Point.point(X = Vector2[j][i][0], Y = Vector2[j][i][1], Height = round(receivedReferenceValues[j][i], 1)))

def SearchForPoints():
    x = 0
    y = 0
    pointsHesh = len(horizontalBots)
    for i in range(pointsHesh):
        dn = int((horizontalBots[i + 1].Height - horizontalBots[i].Height) * 10)
        if dn != 0:
            distance = round(abs(abs(horizontalBots[i].X) - abs(horizontalBots[i + 1].X)) / dn, 1)
            for z in range(dn - 1):
                x = round(horizontalBots[i + z].X + distance, 1)
                horizontalBots.insert(i + z + 1, Point.point(X = x, Y = horizontalBots[i + z].Y, Height = round(horizontalBots[i + z].Height + 0.1, 1))) 
   
    pointsHesh = len(verticalBots)
    for i in range(pointsHesh):
        dn = int((verticalBots[i + 1].Height - verticalBots[i].Height) * 10)
        if dn != 0:
            distance = round(abs(abs(verticalBots[i].Y) - abs(verticalBots[i + 1].Y)) / dn, 1)
            for z in range(dn - 1):
                y = round(verticalBots[i + z].Y - distance, 1)
                verticalBots.insert(i + z + 1, Point.point(X = verticalBots[i + z].X, Y = y, Height = round(verticalBots[i + z].Height+  0.1, 1))) 

       
speed(10)
penup()
goto(-size*3,size*3)
pendown()

def main():
    CreatingPoints()
    SearchForPoints()
       

if __name__ == "__main__":
    main()

mainloop()

