import PySimpleGUI as sg
from upload_data import *
from viz import *

def screen_3(name):
    sg.theme('DarkBlack')

    layout = [[sg.Text()],
              [sg.Text('                                                   '),sg.Text(f'Welcome {name}!', font=('Helvetica', 20, 'bold'),text_color='green')],
              [sg.Text()],
              [sg.Text()],
              [sg.Text()],
              [sg.Text('                                                               '),sg.Button('Add Data', font=('Helvetica', 12, 'bold'),button_color=('green','black'),size=(10,2))],
              [sg.Text()],
              [sg.Text()],
              [sg.Text('                                                               '),sg.Button('Visualizations', font=('Helvetica', 12, 'bold'),button_color=('green','black'),size=(11,2))]
              ]

    # Create the main window
    window = sg.Window('MagneSight', layout,size=(700,500),alpha_channel=0.85)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Add Data':

            file_path = sg.popup_get_file('Select a CSV file', file_types=(("CSV Files", "*.csv"),))
            if file_path:
                up_config_data(file_path)
            window.close()
        if event == 'Visualizations':
            window.close()
            disp_viz()

    window.close()

