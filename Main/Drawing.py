from turtle import *
import sys
import json


receivedReferenceValues = json.loads(sys.argv[1])# массив с данными


speed(10)
size = 100
penup()
#Старт
goto(-size*3,size*3)
pendown()

#Квадрат
goto(size*3,size*3)
goto(size*3,-size*3)
goto(-size*3,-size*3)
goto(-size*3,size*3)

#Столбци
goto(-size*2,size*3)
goto(-size*2,-size*3)
goto(-size,-size*3)
goto(-size,size*3)
goto(0,size*3)
goto(0,-size*3)
goto(size,-size*3)
goto(size,size*3)
goto(size*2,size*3)
goto(size*2,-size*3)
goto(size*3,-size*3)
goto(size*3,size*3)

#Строки
goto(size*3,size*2)
goto(-size*3,size*2)
goto(-size*3,size)
goto(size*3,size)
goto(size*3,0)
goto(-size*3,0)
goto(-size*3,-size)
goto(size*3,-size)
goto(size*3,-size*2)
goto(-size*3,-size*2)
goto(-size*3,-size*3)
goto(size*3,-size*3)

mainloop()