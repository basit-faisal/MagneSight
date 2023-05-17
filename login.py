import PySimpleGUI as sg
from optionsscr import *
import time

def login_page():


    layout = [[sg.Text(background_color='#f1efe7')],
              [sg.Text('                                                     ',background_color='#f1efe7'),sg.Image(filename='Magnesight.png', size=(100, 100), key='-IMAGE-', background_color='#f1efe7')],
              [sg.Text(background_color='#f1efe7')],
              [sg.Text(background_color='#f1efe7')],
              [sg.Text('     ',background_color='#f1efe7'),sg.Text('Username',font=('League Spartan Thin', 15, 'bold'),text_color='#0f0f0f',background_color='#f1efe7'),sg.Text('   ',background_color='#f1efe7'),sg.Input(key='name',size=(40,3),text_color='#0f0f0f')],
              [sg.Text(background_color='#f1efe7')],
              [sg.Text('     ',background_color='#f1efe7'),sg.Text('Password',font=('League Spartan Thin', 15, 'bold'),text_color='#0f0f0f',background_color='#f1efe7'),sg.Text('   ',background_color='#f1efe7'), sg.Input(key='pwd', password_char='*',size=(40,3),text_color='#0f0f0f')],
              [sg.Text(background_color='#f1efe7')],
              [sg.Text(background_color='#f1efe7')],
              [sg.Text('                                                    ', background_color='#f1efe7'),sg.Button('Submit', font=('League Spartan Thin', 12, 'bold'),button_color=('#f1efe7','#0f0f0f'),size=(10,4))]  
              
              
             ]

    # Create the main window
    window = sg.Window('MagneSight', layout,size=(600,400),alpha_channel=0.83, background_color='#f1efe7')

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
