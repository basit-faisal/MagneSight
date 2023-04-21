import pandas as pd
import matplotlib.pyplot as plt

def create_viz(file_path):
    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path).head(10)
    #BAR CHART
    df.plot(kind='bar', x='City', y='gross income')
    plt.show()

    #LINE CHART
    df.plot(kind='line',x='City', y='Unit price')
    plt.show
    
    #Scatter Plot
    df.plot(kind='scatter', x='Quantity', y='Unit price')
    plt.show()
    
    #Pie Chart
    sales_by_product = df.groupby('Product line')['Total'].sum()

    # Create a pie chart of the sales by product line
    plt.pie(sales_by_product, labels=sales_by_product.index, autopct='%1.1f%%')
    plt.title('Sales by Product Line')
    plt.show()
    
    #Box Plot
  
    # Select the columns you want to create the box plot for
    boxplot_cols = ['cogs']

    # Create the box plot using the selected columns
    df[boxplot_cols].plot(kind='box')

    # Set the title and axis labels
    plt.title('Box Plot of COGS')
    plt.ylabel('Price/Quantity/Percentage')
    plt.show()

    #histogram
    
    df.plot(kind='hist', y='Unit price', bins=10)
    plt.title('')
    plt.show()
    
