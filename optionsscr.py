import PySimpleGUI as sg
from upload_data import *
from viz import *
import os

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

    # Initialize the last selected directory path
    last_dir_path = ''

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Add Data':
            # Open file explorer and get file path
            file_path = sg.popup_get_file('Select a CSV file', initial_folder=last_dir_path, file_types=(("CSV Files", "*.csv"),))
            
            if file_path:
                # Update last selected directory path
                last_dir_path = os.path.dirname(file_path)

                # Pass file path to upload_data function
                #up_config_data(file_path)
                
            continue
        if event == 'Visualizations':
            # Open file explorer and get file path
            #file_path = sg.popup_get_file('Select a CSV file', initial_folder=last_dir_path, file_types=(("CSV Files", "*.csv"),))

            if file_path:
                # Update last selected directory path
                last_dir_path = os.path.dirname(file_path)

                # Call the create_viz function from the viz module
                create_viz(file_path)
                
            continue

    # Close the main window and exit the program
    window.close()
