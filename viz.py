import pandas as pd
import matplotlib.pyplot as plt

def create_viz(file_path):
    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path).head(10)
    #BAR CHART
    df.plot(kind='bar', x='City', y='Unit price')
    plt.show()

    #LINE CHART
    df.plot(kind='line',x='City', y='Unit price')
    plt.show
    
    #Scatter Plot
    df.plot(kind='scatter', x='City', y='Unit price')
    plt.show()
    
    #Pie Chart
    df.plot(kind='pie', y='Unit price', labels=df['City'])
    plt.show()
    
    #Box Plot
    df.plot(kind='box', y='Unit price')
    plt.show()

    #histogram
    df.plot(kind='hist', y='Unit price', bins=10)
    plt.show()
    
