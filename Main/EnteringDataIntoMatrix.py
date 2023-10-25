import flet as ft
import time 
import subprocess
import sys
import json

def main(page: ft.Page):
    page.title = "Flet counter example"
    
    widthText = 70
    heightText = 40
    
    #создаём текстовые поля 
    textFields = [
        [
            ft.TextField(label="0/0", width=widthText, height=heightText),
            ft.TextField(label="0/1", width=widthText, height=heightText),
            
            ft.TextField(label="0/2", width=widthText, height=heightText),
            ft.TextField(label="0/3", width=widthText, height=heightText),
    
            ft.TextField(label="0/4", width=widthText, height=heightText),
            ft.TextField(label="0/5", width=widthText, height=heightText),
            
            ft.TextField(label="0/6", width=widthText, height=heightText),
        ],
        [
            ft.TextField(label="1/0", width=widthText, height=heightText),
            ft.TextField(label="1/1", width=widthText, height=heightText),
            
            ft.TextField(label="1/2", width=widthText, height=heightText),
            ft.TextField(label="1/3", width=widthText, height=heightText),
            
            ft.TextField(label="1/4", width=widthText, height=heightText),
            ft.TextField(label="1/5", width=widthText, height=heightText),
            
            ft.TextField(label="1/6", width=widthText, height=heightText),
        ],
        [
            ft.TextField(label="2/0", width=widthText, height=heightText),
            ft.TextField(label="2/1", width=widthText, height=heightText),
            
            ft.TextField(label="2/2", width=widthText, height=heightText),
            ft.TextField(label="2/3", width=widthText, height=heightText),
            
            ft.TextField(label="2/4", width=widthText, height=heightText),
            ft.TextField(label="2/5", width=widthText, height=heightText),
        
            ft.TextField(label="2/6", width=widthText, height=heightText),
        ],
        [
            ft.TextField(label="3/0", width=widthText, height=heightText),
            ft.TextField(label="3/1", width=widthText, height=heightText),
            
            ft.TextField(label="3/2", width=widthText, height=heightText),
            ft.TextField(label="3/3", width=widthText, height=heightText),
            
            ft.TextField(label="3/4", width=widthText, height=heightText),
            ft.TextField(label="3/5", width=widthText, height=heightText),
            
            ft.TextField(label="3/6", width=widthText, height=heightText),
        ],
        [
            ft.TextField(label="4/0", width=widthText, height=heightText),
            ft.TextField(label="4/1", width=widthText, height=heightText),
            
            ft.TextField(label="4/2", width=widthText, height=heightText),
            ft.TextField(label="4/3", width=widthText, height=heightText),
            
            ft.TextField(label="4/4", width=widthText, height=heightText),
            ft.TextField(label="4/5", width=widthText, height=heightText),
            
            ft.TextField(label="4/6", width=widthText, height=heightText),
        ],
        [
            ft.TextField(label="5/0", width=widthText, height=heightText),
            ft.TextField(label="5/1", width=widthText, height=heightText),
            
            ft.TextField(label="5/2", width=widthText, height=heightText),
            ft.TextField(label="5/3", width=widthText, height=heightText),
            
            ft.TextField(label="5/4", width=widthText, height=heightText),
            ft.TextField(label="5/5", width=widthText, height=heightText),
            
            ft.TextField(label="5/6", width=widthText, height=heightText),
        ],
        [
            ft.TextField(label="6/0", width=widthText, height=heightText),
            ft.TextField(label="6/1", width=widthText, height=heightText),
        
            ft.TextField(label="6/2", width=widthText, height=heightText),
            ft.TextField(label="6/3", width=widthText, height=heightText),
        
            ft.TextField(label="6/4", width=widthText, height=heightText),
            ft.TextField(label="6/5", width=widthText, height=heightText),
        
            ft.TextField(label="6/6", width=widthText, height=heightText),
        ],
    ]
    
    page.window_width = 580 # Задаем ширину окна
    page.window_height = 600 # Задаем высоту окна
    page.window_resizable = False # Запрещаем изменять размеры окна
    page.update()
    
    #добавляем текстовые поля в интерфейс
    page.add(ft.Row(
        [
            textFields[0][0],
            textFields[0][1],
            textFields[0][2],
            textFields[0][3],
            textFields[0][4],
            textFields[0][5],
            textFields[0][6],
        ]))
    page.add(ft.Row(
        [
            textFields[1][0],
            textFields[1][1],
            textFields[1][2],
            textFields[1][3],
            textFields[1][4],
            textFields[1][5],
            textFields[1][6],
        ]))
    page.add(ft.Row(
        [
            textFields[2][0],
            textFields[2][1],
            textFields[2][2],
            textFields[2][3],
            textFields[2][4],
            textFields[2][5],
            textFields[2][6],
        ]))
    page.add(ft.Row(
        [
            textFields[3][0],
            textFields[3][1],
            textFields[3][2],
            textFields[3][3],
            textFields[3][4],
            textFields[3][5],
            textFields[3][6],
        ]))
    page.add(ft.Row(
        [
            textFields[4][0],
            textFields[4][1],
            textFields[4][2],
            textFields[4][3],
            textFields[4][4],
            textFields[4][5],
            textFields[4][6],
        ]))
    page.add(ft.Row(
        [
            textFields[5][0],
            textFields[5][1],
            textFields[5][2],
            textFields[5][3],
            textFields[5][4],
            textFields[5][5],
            textFields[5][6],
        ]))
    page.add(ft.Row(
        [
            textFields[6][0],
            textFields[6][1],
            textFields[6][2],
            textFields[6][3],
            textFields[6][4],
            textFields[6][5],
            textFields[6][6], 
        ]))
    
    referenceValues=[[],[],[],[],[],[],[]]
    
    
    def Start(e):
        erorr = False
        
        for i in range(len(textFields)):
            for j in range(len(textFields[i])):
                if textFields[i][j].value == "":
                    erorr = True
                else:
                    if len(referenceValues[i]) < len(textFields[i]):
                        referenceValues[i].append([])
                    referenceValues[i][j] = float(textFields[i][j].value)
        
        #if erorr == True:
        #    startButton.text = "ERROR"
        #    page.update()
        #    time.sleep(3)
        #    startButton.text = "start"
        #    page.update()  
        #else:
        jsonReferenceValues = json.dumps(referenceValues)
        subprocess.call(["python", "Drawing.py", jsonReferenceValues])      
        sys.exit()
    
    startButton = ft.TextButton(text="start", width=100, height=50, on_click=Start)
    
    page.add(ft.Row([startButton]))

ft.app(target=main)