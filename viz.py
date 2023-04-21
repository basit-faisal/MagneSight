import pandas as pd
import folium
import webbrowser
import folium.plugins
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim


def create_viz(file_path):
    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path).head(20)    
    #----------------------Stacked Bar Chart  ------------------  
    grouped_data = df.groupby(['Gender', 'Product line']).size().unstack()
    # Create a stacked bar chart using pandas
    ax = grouped_data.plot(kind='bar', stacked=True, figsize=(10, 6))
    # Set the chart title and axis labels
    ax.set_title('Product Line by Gender')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Count')
    plt.show()

    #----------------------LINE CHART------------------------------
    #Convert the Date column to a datetime object and set it as the index
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    # Group the data by month and sum the quantity sold
    monthly_quantity = df.resample('M')['Quantity'].sum()
    ax = monthly_quantity.plot(kind='line', figsize=(10, 6))
    ax.set_title('Monthly Quantity Sold')
    ax.set_xlabel('Month')
    ax.set_ylabel('Quantity Sold')
    plt.show()

    #----------------------Scatter Plot---------------------------
    ax = df.plot(kind='scatter', x='Unit price', y='Quantity', figsize=(10, 6))
    ax.set_title('Quantity of Products Sold Based on Unit Price')
    ax.set_xlabel('Unit Price')
    ax.set_ylabel('Quantity')
    plt.show()

    #----------------------Pie Chart------------------------------
    sales_by_product = df.groupby('Product line')['Total'].sum()
    plt.pie(sales_by_product, labels=sales_by_product.index, autopct='%1.1f%%')
    plt.title('Sales by Product Line')
    plt.show()
    
    #------------------------Box Plot-----------------------------
    # Select the columns you want to create the box plot for
    boxplot_cols = ['cogs']
    # Create the box plot using the selected columns
    df[boxplot_cols].plot(kind='box')
    # Set the title and axis labels
    plt.title('Box Plot of Cost of Goods Sold')
    plt.ylabel('Price/Quantity/Percentage')
    plt.show()

    #----------------displaying on folium map---------------
    # Get the total sales for each city
    city_sales = df.groupby('City')['Total'].sum()

    # Get a list of unique city names from the DataFrame
    cities = city_sales.index.tolist()

    # Define the function for converting city names to latitudes and longitudes
    def lon_lat(data):
        latitude = []
        longitude = []
        geolocator = Nominatim(user_agent="my_app")
        for value in data:
            location = geolocator.geocode(value)
            latitude.append(location.latitude)
            longitude.append(location.longitude)
        return latitude, longitude

    # Convert the city names to latitudes and longitudes
    lat, lon = lon_lat(cities)

    # Create a dictionary of city sales for the heatmap
    city_sales_dict = {city: sales for city, sales in zip(cities, city_sales)}

    # Determine the highest and lowest sales values
    max_sales = max(city_sales)
    min_sales = min(city_sales)

    # Create the map and add the markers layer
    world_map = folium.Map(location=[sum(lat)/len(lat), sum(lon)/len(lon)], zoom_start=7)

    markers_layer = folium.FeatureGroup(name='Markers')

    for city, sales, latitude, longitude in zip(cities, city_sales, lat, lon):
        if sales == max_sales:
            color = 'red'
        elif sales == min_sales:
            color = 'green'
        else:
            color = 'orange'
        marker = folium.Marker(location=[latitude, longitude], tooltip=city, icon=folium.Icon(color=color))
        marker.add_to(markers_layer)

    # Add the markers layer to the map and enable layer control
    world_map.add_child(markers_layer)
    folium.LayerControl().add_to(world_map)

    # Save the map to an HTML file and open it in a web browser
    world_map.save('map.html')
    webbrowser.open('map.html')

        
    
