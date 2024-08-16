import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Import the data
url = 'https://raw.githubusercontent.com/NikoStein/pds_data/main/sales.csv'
data = pd.read_csv(url, parse_dates=['Date'])

# Step 2: Total Sales per Store for the Year 2014
data_2014 = data[data['Date'].dt.year == 2014]
total_sales_2014 = data_2014.groupby('Store')['Sales'].sum()

# Step 3: Store with the Most Consistent Sales
sales_std_dev = data.groupby('Store')['Sales'].std()
most_consistent_store = sales_std_dev.idxmin()
most_consistent_sales_std_dev = sales_std_dev.min()

# Step 4: Monthly Sales Trend for Each Store
data['YearMonth'] = data['Date'].dt.to_period('M')
monthly_sales_trend = data.groupby(['Store', 'YearMonth'])['Sales'].sum().reset_index()
monthly_sales_trend['YearMonth'] = monthly_sales_trend['YearMonth'].astype(str)

# Step 5: Sales Distribution by Day of the Week
data['DayOfWeek'] = data['Date'].dt.day_name()
average_sales_by_day = data.groupby('DayOfWeek')['Sales'].mean().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
)

# Plotting the average sales by day of the week
plt.figure(figsize=(10, 6))
average_sales_by_day.plot(kind='bar')
plt.title('Average Sales by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Average Sales')
plt.show()
plt.savefig('average_sales_by_day.png')

# Step 6: Sales Trend for the Top 5 Stores
top_5_stores = total_sales_2014.nlargest(5).index
top_5_data = data[data['Store'].isin(top_5_stores)]

# Plotting the sales trend for the top 5 stores
plt.figure(figsize=(12, 8))
for store in top_5_stores:
    store_data = top_5_data[top_5_data['Store'] == store]
    store_data = store_data.groupby('Date')['Sales'].sum().reset_index()
    plt.plot(store_data['Date'], store_data['Sales'], label=f'Store {store}')

plt.title('Sales Trend for the Top 5 Stores')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.show()
plt.savefig('sales_trend_top_5_stores.png')

# Output results
print("Total Sales per Store for the Year 2014:")
print(total_sales_2014)

print("\nStore with the Most Consistent Sales:")
print(f"Store: {most_consistent_store}, SalesStdDev: {most_consistent_sales_std_dev}")

print("\nMonthly Sales Trend for Each Store:")
print(monthly_sales_trend)

print("\nAverage Sales by Day of the Week:")
print(average_sales_by_day)