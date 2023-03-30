import PySimpleGUI as sg

def disp_viz(*args):
    sg.theme('DarkBlack')

    layout = [[sg.Text()],
              [sg.Text('                                                   '),sg.Text(f'Welcome!', font=('Helvetica', 20, 'bold'),text_color='green')],
              [sg.Text()]]
    
    window = sg.Window('MagneSight', layout,size=(700,500),alpha_channel=0.85)


    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
    
    window.close()