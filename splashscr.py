import PySimpleGUI as sg
from login import *
import time
from PIL import Image

#Define the layout of the splash screen
layout = [
    [sg.Text('   ',background_color='#f1efe7')],
    [sg.Text('   ',background_color='#f1efe7')],
    [sg.Text('   ',background_color='#f1efe7')],
    [sg.Text('   ', background_color='#f3ebe3'), sg.Image(filename='logo.png', size=(600, 250), key='-IMAGE-', background_color='#f1efe7')],
    [sg.Text( font=('League Spartan Thin', 30, 'bold'), justification='center', text_color='#0f0f0f', background_color='#f1efe7')],
    [sg.ProgressBar(100, orientation='h', size=(40, 20), key='progressbar', bar_color=('#0f0f0f', 'white'))],
    [sg.Text('   ',background_color='#f1efe7')],
    [sg.Text('   ',background_color='#f1efe7')],

]



# Create the splash screen window
splash_window = sg.Window('MagneSight', layout, no_titlebar=True, finalize=True, alpha_channel=0.83, background_color='#f1efe7', element_justification='c')

# Simulate loading process
for i in range(101):
    event, values = splash_window.read(timeout=10)
    if event == sg.WINDOW_CLOSED:
        break
    splash_window['progressbar'].update(i)
    if i == 100:
        time.sleep(2)
        break

# Close the splash screen window
splash_window.close()

login_page()

print()
