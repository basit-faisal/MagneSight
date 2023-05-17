import PySimpleGUI as sg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor, plot_tree, DecisionTreeClassifier, export_graphviz
import graphviz
from sklearn import tree
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.preprocessing import OneHotEncoder


#prediction library needed

def FinalScreen(file_path):
    

    layout = [[sg.Text(background_color='#f1efe7')],
              [sg.Text('                                                ', background_color='#f1efe7'),sg.Text('X - SEARCH', font=('League Spartan Thin Black', 20, 'bold'),text_color='black', background_color='#f1efe7')],
              [sg.Text(background_color='#f1efe7')],
              [sg.Text(background_color='#f1efe7')],
              [sg.Text('          ', background_color='#f1efe7'),sg.Text('Invoice ID',font=('League Spartan Thin', 13, 'bold'),text_color='black', background_color='#f1efe7'),sg.Input(key='name',size=(40,3),text_color='black')],
              [sg.Text(background_color='#f1efe7')],
              [sg.Text(background_color='#f1efe7')],
              [sg.Text('                                                      ',background_color='#f1efe7'),sg.Button('Search', font=('League Spartan Thin', 13, 'bold'),button_color=('#f1efe7','black'),size=(9,1))],
              [sg.Text(background_color='#f1efe7')],
              [sg.Text('                                                      ', background_color='#f1efe7'),sg.Button('Predict', font=('League Spartan Thin', 13, 'bold'),button_color=('#f1efe7','black'),size=(9,1))]  
             ]
    
    window = sg.Window('MagneSight', layout,size=(600,400),alpha_channel=0.83,icon=r'C:\Users\LENOVO\Desktop\ds-proj\code\aa.ico', background_color='#f1efe7')
    
    df = pd.read_csv(file_path) 
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Search':
            # Get the search value entered by the user
            search_value = values['name']
            result_df = df[df['Invoice ID'] == search_value]
            # Output all the other values in the row that matches the search value
            if not result_df.empty:
                output_str = f"Invoice ID: '{search_value}':\n{result_df.iloc[0]}"
                sg.popup(output_str, title='Search Result', background_color='#f1efe7', button_color='black', text_color='black')
            else:
                sg.popup(f"No rows found with that Invoice ID: '{search_value}'", title='Search Result',background_color='#f1efe7', button_color='black', text_color='black')

            pass
        elif event == 'Predict':
                      
            # Linear Regression Model[COGS VS Gross INCome]                
            train = df.sample(frac=0.8, random_state=1)
            test = df.drop(train.index)
            model = LinearRegression()
            model.fit(train[['cogs']], train['gross income'])

            
            cogs_pred = np.linspace(0, 3000, 100)# adjust range and number of points as needed
            # gender_code = np.full_like(cogs_pred, test['gender_code'].iloc[0])
            # quant_pred = np.full_like(cogs_pred, test['Quantity'].iloc[0])
            X_pred_cogs = pd.DataFrame({'cogs': cogs_pred})
            y_pred_cogs = model.predict(X_pred_cogs)
            
            
            plt.scatter(test['cogs'], test['gross income'], color='black', label='Actual')
            plt.scatter(cogs_pred, y_pred_cogs, color='red', label='Predicted')
            plt.title('Linear Regression [COGS Affecting Gross Income]')
            plt.xlabel('Cost of Goods Sold')
            plt.ylabel('Gross Income')
            m, b = np.polyfit(test['cogs'], test['gross income'], 1)
            plt.plot(cogs_pred, m*cogs_pred + b)
            plt.legend()
            plt.show()    
            
            
            
            # Decision Tree Model
            
            X =pd.get_dummies(df['Gender'])
            y = df['Payment']
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

            clf= DecisionTreeClassifier()
            clf = clf.fit(X_train, y_train)

            
            # dot_data = export_graphviz(clf, out_file=None,
            #                feature_names=X.columns,
            #                class_names=y.unique(),
            #                filled=True, rounded=True,
            #                special_characters=True)

            # dot_data = dot_data.replace('digraph Tree {', 'digraph Tree { graph [label="Decision Tree for Gender and Payment"];\n')

            # graph = graphviz.Source(dot_data)
            # graph.render("decision_tree")


            # graph.render(view=True)
            
            fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (3,3), dpi=200)
            plot_tree(clf,
               feature_names = X.columns, 
               class_names=y.unique(),
               filled = True);
            plt.title("Decision Tree for Gender and Payment")
            plt.show()
            
            #LAST ML basically visualizing which products does each gender buy, if there were more products in dataset we can easily find out if there is a product males buy and females don't and vicerversa
            # One-Hot Encode categorical variables
            encoder = OneHotEncoder()
            df_encoded = encoder.fit_transform(df[['Gender', 'Product line']]).toarray()

            # Create a separate dataframe with the encoded features
            df_encoded = pd.DataFrame(df_encoded, columns=encoder.get_feature_names_out(['Gender', 'Product line']))
            df_cat = df[['Gender', 'Product line']]
            df_cat.reset_index(drop=True, inplace=True)
            df_encoded.reset_index(drop=True, inplace=True)
            df_cat_encoded = pd.concat([df_cat, df_encoded], axis=1)

            # Concatenate the encoded features with the original dataframe
            df = pd.concat([df, df_encoded], axis=1)

            # Drop unnecessary columns
            df = df.drop(['Invoice ID', 'Branch', 'City', 'Customer type', 'Unit price', 'Quantity', 'Tax 5%', 'Total', 'Date', 'Time', 'Payment', 'cogs', 'gross margin percentage', 'gross income', 'Rating', 'Gender', 'Product line'], axis=1)

            # Scale the data
            scaler = StandardScaler()
            df_scaled = scaler.fit_transform(df)

            # Fit K-Means clustering model
            kmeans = KMeans(n_clusters=2, random_state=0)
            kmeans.fit(df_scaled)

            # Add the cluster labels to the dataframe
            df_cat_encoded['Cluster'] = kmeans.labels_

            # Plot the clusters
            plt.figure(figsize=(10,10))
            plt.scatter(df_cat_encoded['Product line'], df_cat_encoded['Gender'], c=df_cat_encoded['Cluster'], cmap='rainbow')
            plt.title('Clustering customers based on Product line and Gender',fontsize=15,fontweight="bold")
            plt.xlabel('Product line')
            plt.ylabel('Gender')
            plt.show()

    window.close()
    

#linear_reg()
