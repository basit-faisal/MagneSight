import PySimpleGUI as sg
from optionsscr import *
import time

def login_page():
    sg.theme('DarkBlack')

    layout = [[sg.Text()],
              [sg.Text('                            '),sg.Text('Welcome to MagneSight!', font=('Helvetica', 20, 'bold'),text_color='green')],
              [sg.Text()],
              [sg.Text('                                                       '),sg.Text("LOGIN",font=('Helvetica', 17, 'bold'),text_color='green')],
              [sg.Text()],
              [sg.Text()],
              [sg.Text('   '),sg.Text('Username',font=('Helvetica', 13, 'bold'),text_color='green'),sg.Text('   '),sg.Input(key='name',size=(40,3),text_color='limegreen')],
              [sg.Text()],
              [sg.Text('   '),sg.Text('Password',font=('Helvetica', 13, 'bold'),text_color='green'),sg.Text('   '), sg.Input(key='pwd', password_char='*',size=(40,3),text_color='limegreen')],
              [sg.Text()],
              [sg.Text()],
              [sg.Text('                                                    '),sg.Button('Submit', font=('Helvetica', 12, 'bold'),button_color=('green','black'),size=(9,1))]  
              
              
             ]

    # Create the main window
    window = sg.Window('MagneSight', layout,size=(600,400),alpha_channel=0.83)

    # Display the main window
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Submit':
            if values['name'] == 'admin' and values['pwd'] == 'admin':
                NAME = values['name']
                time.sleep(2)
                window.close()
                screen_3(NAME)
                
            else:
                if values['name'] != 'admin' and values['pwd'] == 'admin':
                    sg.popup("Incorrect Name, try again")
                    window['name'].update('')
                elif values['name'] == 'admin' and values['pwd'] != 'admin':
                    sg.popup("Incorrect password, try again")
                    window['pwd'].update('')
                else:
                    sg.popup('Incorrect name and password. please try again')
                    window['name'].update('')
                    window['pwd'].update('')



    # Close the main window and exit the program
    window.close()
