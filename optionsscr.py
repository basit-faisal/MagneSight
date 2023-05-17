import PySimpleGUI as sg

from viz import *
import os
from search_query import *
def screen_3(name):

    layout = [[sg.Text(background_color='#f1efe7')],
              [sg.Text('                                               ', background_color='#f1efe7'),sg.Text(f'Welcome {name}!', font=('League Spartan Thin Black', 28, 'bold'),text_color='black', background_color='#f1efe7')],
              [sg.Text(background_color='#f1efe7')],
              [sg.Text(background_color='#f1efe7')],
              [sg.Text(background_color='#f1efe7')],
              [sg.Text('                                                        ', background_color='#f1efe7'),sg.Button('Add Data', font=('League Spartan Thin', 15, 'bold'),button_color=('#f1efe7','#000000'),size=(16,1),border_width=2, pad=(0,0))],
              [sg.Text(background_color='#f1efe7')],
              [sg.Text(background_color='#f1efe7')],
              [sg.Text('                                                         ', background_color='#f1efe7'),sg.Button('Visualizations', font=('League Spartan Thin', 15, 'bold'),button_color=('#f1efe7','#000000'),size=(16,1),border_width=2, pad=(0,0))],
              [sg.Text(background_color='#f1efe7')],
              [sg.Text(background_color='#f1efe7')],
              [sg.Text(background_color='#f1efe7')],
              [sg.Text(background_color='#f1efe7')],
              [sg.Text(background_color='#f1efe7')],
              [sg.Text('                                                                                                                                            ', background_color='#f1efe7'),sg.Button('Next', font=('League Spartan Thin', 16, 'bold'),button_color=('#f1efe7','black'),size=(11,1))]
              
              
              ]


    # Create the main window
    window = sg.Window('MagneSight', layout,size=(700,550),alpha_channel=0.85, background_color='#f1efe7')

    # Initialize the last selected directory path
    last_dir_path = ''
    file_path = None
    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'Add Data':
            # Open file explorer and get file path
            file_path = sg.popup_get_file('Select a CSV file', initial_folder=last_dir_path, file_types=(("CSV Files", "*.csv"),),background_color='#f1efe7',text_color='black' , button_color='black')
            
            if file_path:
                # Update last selected directory path
                last_dir_path = os.path.dirname(file_path)

                # Pass file path to upload_data function
                #up_config_data(file_path)
                
            continue
        elif event == 'Visualizations':
            if file_path == None:
                sg.popup("Load Data First!",background_color='#f1efe7',text_color='black', button_color='black' )
            # Open file explorer and get file path
            #file_path = sg.popup_get_file('Select a CSV file', initial_folder=last_dir_path, file_types=(("CSV Files", "*.csv"),))
            else:

                if file_path:
                # Update last selected directory path
                    last_dir_path = os.path.dirname(file_path)

                # Call the create_viz function from the viz module
                    create_viz(file_path)

            continue
        elif event == 'Next':
            if file_path == None:
                sg.popup("Load Data First!",background_color='#f1efe7', text_color='black', button_color='black')
            else:
                window.close()
                FinalScreen(file_path)    
            
            #lazzy(file_path)
            
            continue



    # Close the main window and exit the program
    window.close()
