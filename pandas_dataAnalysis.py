import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load the e-commerce sales data from CSV
sales_data = pd.read_csv('ecommerce_sales_data.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(sales_data.head())

# Basic statistics of the dataset
print("\nBasic statistics of the dataset:")
print(sales_data.describe())

# Check for missing values
print("\nMissing values in the dataset:")
print(sales_data.isnull().sum())

# Convert the 'Order Date' column to datetime format
sales_data['Order Date'] = pd.to_datetime(sales_data['Order Date'])

# Extracting month and year from 'Order Date'
sales_data['Month'] = sales_data['Order Date'].dt.month
sales_data['Year'] = sales_data['Order Date'].dt.year

# Total sales per month
monthly_sales = sales_data.groupby(['Year', 'Month'])[
    'Sales'].sum().reset_index()

# Visualize monthly sales
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales['Month'], monthly_sales['Sales'],
         marker='o', linestyle='-')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.xticks(np.arange(1, 13), ['Jan', 'Feb', 'Mar', 'Apr',
           'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(True)
plt.show()

# Product performance analysis
product_performance = sales_data.groupby(
    'Product')['Quantity Ordered', 'Sales'].sum().reset_index()
product_performance['Average Price'] = product_performance['Sales'] / \
    product_performance['Quantity Ordered']

# Visualize top selling products
top_products = product_performance.sort_values(
    by='Quantity Ordered', ascending=False).head(10)
plt.figure(figsize=(12, 6))
plt.bar(top_products['Product'], top_products['Quantity Ordered'])
plt.title('Top 10 Best Selling Products')
plt.xlabel('Product')
plt.ylabel('Quantity Ordered')
plt.xticks(rotation=45, ha='right')
plt.show()
