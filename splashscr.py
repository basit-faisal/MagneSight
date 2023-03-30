import PySimpleGUI as sg
from login import *
import time

sg.theme('DarkBlack')

# Define the layout of the splash screen
layout = [[sg.Text()],
          [sg.Text('   '),sg.Image(filename='aa.png', size=(400, 200), key='-IMAGE-')],
          [sg.Text('Loading', font=('Helvetica', 20, 'bold italic'), justification='center',text_color='green')],
          [sg.ProgressBar(100, orientation='h', size=(40, 20), key='progressbar',bar_color=('green','white'))]
          
        ]
          

# Create the splash screen window
splash_window = sg.Window('MagneSight', layout, no_titlebar=True, finalize=True, alpha_channel=0.83)

# Simulate loading process
for i in range(101):
    event, values = splash_window.read(timeout=10)
    if event == sg.WIN_CLOSED:
        break
    splash_window['progressbar'].update(i)
    if i == 100:
        time.sleep(2)
        break

# Close the splash screen window
splash_window.close()

login_page()