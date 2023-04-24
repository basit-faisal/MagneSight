import PySimpleGUI as sg
import pandas as pd
#prediction library needed




def final_screen():
    
    sg.theme('DarkBlack')

    layout = [[sg.Text()],
              [sg.Text('                                               '),sg.Text('X - SEARCH', font=('Helvetica', 20, 'bold'),text_color='green')],
              [sg.Text()],
              [sg.Text()],
              [sg.Text('   '),sg.Text('Username / ID',font=('Helvetica', 13, 'bold'),text_color='green'),sg.Input(key='name',size=(40,3),text_color='limegreen')],
              [sg.Text()],
              [sg.Text()],
              [sg.Text('                                                    '),sg.Button('Search', font=('Helvetica', 12, 'bold'),button_color=('green','black'),size=(9,1))],
              [sg.Text()],
              [sg.Text('                                                    '),sg.Button('Predict', font=('Helvetica', 12, 'bold'),button_color=('green','black'),size=(9,1))]  
             ]
    
    window = sg.Window('MagneSight', layout,size=(600,400),alpha_channel=0.83,icon=r'C:\Users\LENOVO\Desktop\ds-proj\code\aa.ico')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Submit':
            pass
        elif event == 'predict':
            pass
    

    window.close()

#final_screen()