import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    
    widthText = 70
    heightText = 40
    
    #создаём текстовые поля 
    text_fields = [
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
    
    
    referenceValues = [
        [],
        [],
        [],
        [],
        [],
        []
    ]
    
    page.window_width = 580 # Задаем ширину окна
    page.window_height = 600 # Задаем высоту окна
    page.window_resizable = False # Запрещаем изменять размеры окна
    page.update()
    
    #добавляем текстовые поля в интерфейс
    page.add(ft.Row(
        [
            text_fields[0][0],
            text_fields[0][1],
            text_fields[0][2],
            text_fields[0][3],
            text_fields[0][4],
            text_fields[0][5],
            text_fields[0][6],
        ]))
    page.add(ft.Row(
        [
            text_fields[1][0],
            text_fields[1][1],
            text_fields[1][2],
            text_fields[1][3],
            text_fields[1][4],
            text_fields[1][5],
            text_fields[1][6],
        ]))
    page.add(ft.Row(
        [
            text_fields[2][0],
            text_fields[2][1],
            text_fields[2][2],
            text_fields[2][3],
            text_fields[2][4],
            text_fields[2][5],
            text_fields[2][6],
        ]))
    page.add(ft.Row(
        [
            text_fields[3][0],
            text_fields[3][1],
            text_fields[3][2],
            text_fields[3][3],
            text_fields[3][4],
            text_fields[3][5],
            text_fields[3][6],
        ]))
    page.add(ft.Row(
        [
            text_fields[4][0],
            text_fields[4][1],
            text_fields[4][2],
            text_fields[4][3],
            text_fields[4][4],
            text_fields[4][5],
            text_fields[4][6],
        ]))
    page.add(ft.Row(
        [
            text_fields[5][0],
            text_fields[5][1],
            text_fields[5][2],
            text_fields[5][3],
            text_fields[5][4],
            text_fields[5][5],
            text_fields[5][6],
        ]))
    page.add(ft.Row(
        [
            text_fields[6][0],
            text_fields[6][1],
            text_fields[6][2],
            text_fields[6][3],
            text_fields[6][4],
            text_fields[6][5],
            text_fields[6][6], 
        ]))

    page.add(ft.Row([ft.ElevatedButton("start", width=100, height=50)]))

ft.app(target=main)