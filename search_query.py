import PySimpleGUI as sg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from lazypredict.Supervised import LazyRegressor

#prediction library needed

def FinalScreen(file_path):
    
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
    
    df = pd.read_csv(file_path) 
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Submit':
            
            

            pass
        elif event == 'Predict':
            df['gender_code'] = df['Gender'].map({'Male': 1, 'Female': 0})           

            
            train = df.sample(frac=0.8, random_state=1)
            test = df.drop(train.index)
            model = LinearRegression()
            
            model.fit(train[['cogs','gender_code', 'Quantity']], train['gross income'])
            print('Coefficients:', model.coef_)
            print('Intercept:', model.intercept_)
            y_pred = model.predict(test[['cogs', 'gender_code', 'Quantity']])
            

            plt.scatter(test['gender_code'], test['gross income'],color='black')
            plt.title('Linear Regression [Gender Affecting Gross Income]')
            plt.xlabel('Gender')
            plt.ylabel('gross income')
            m, b = np.polyfit(test['gender_code'], test['gross income'], 1)
            plt.plot(test['gender_code'], m*test['gender_code'] + b)
            plt.show()
            
            plt.scatter(test['cogs'], test['gross income'],color='black')
            plt.title('Linear Regression [COGS Affecting Gross Income]')
            plt.xlabel('Cost of Goods Sold')
            plt.ylabel('gross income')
            m, b = np.polyfit(test['cogs'], test['gross income'], 1)
            plt.plot(test['cogs'], m*test['cogs'] + b)
            plt.show()

            plt.scatter(test['Quantity'], test['gross income'],color='black')
            plt.title('Linear Regression [Quantity Affecting Gross Income]')
            plt.xlabel('Quantity')
            plt.ylabel('gross income')
            m, b = np.polyfit(test['Quantity'], test['gross income'], 1)
            plt.plot(test['Quantity'], m*test['Quantity'] + b)
            plt.show()
    window.close()
    

#linear_reg()
