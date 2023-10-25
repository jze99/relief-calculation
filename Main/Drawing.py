from turtle import *
import sys
import json


receivedReferenceValues = json.loads(sys.argv[1])# массив с данными

size = 100

Vector2 = [
    [[-size*3,size*3],[-size*2,size*3],[-size,size*3],[0,size*3],[size,size*3],[size*2,size*3],[size*3,size*3]],
    [[-size*3,size*2],[-size*2,size*2],[-size,size*2],[0,size*2],[size,size*2],[size*2,size*2],[size*3,size*2]],
    [[-size*3,size],[-size*2,size],[-size,size],[0,size],[size,size],[size*2,size],[size*3,size]],
    [[-size*3,0],[-size*2,0],[-size,0],[0,0],[size,0],[size*2,0],[size*3,0]],
    [[-size*3,-size],[-size*2,-size],[-size,-size],[0,-size],[size,-size],[size*2,-size],[size*3,-size]],
    [[-size*3,-size*2],[-size*2,-size*2],[-size,-size*2],[0,-size*2],[size,-size*2],[size*2,-size*2],[size*3,-size*2]],
    [[-size*3,-size*3],[-size*2,-size*3],[-size,-size*3],[0,-size*3],[size,-size*3],[size*2,-size*3],[size*3,-size*3]]
    ]

speed(10)
penup()
goto(-size*3,size*3)
pendown()

#Квадрат
for i in range(len(Vector2)):
    t = len(Vector2[i])
    for j in range(len(Vector2[i])):
        if i%2==0:
            goto(-Vector2[i][j][0],Vector2[i][j][1])
            t-=1
            write(receivedReferenceValues[i][t])
        else:
            goto(Vector2[i][j][0],Vector2[i][j][1])
            write(receivedReferenceValues[i][j])
        
    
    
penup()
goto(-size*3,size*3)
pendown()  
            
for i in range(len(Vector2)):
    for j in range(len(Vector2[i])):
        if i%2 != 0:
            goto(Vector2[j][i][0], -Vector2[j][i][1])
        else:
            goto(Vector2[j][i][0], Vector2[j][i][1])



mainloop()