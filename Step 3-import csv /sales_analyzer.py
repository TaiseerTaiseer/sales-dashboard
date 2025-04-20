import pandas as pd

# Load CSV into DataFrame
df = pd.read_csv("sales.csv")

# Show first few rows
print("Full Data:")
print(df)

# Add a new column: Total = Quantity * Price
df["Total"] = df["Quantity"] * df["Price"]

# Show total revenue
total_revenue = df["Total"].sum()
print("\n💰 Total Revenue:", total_revenue)

# Group by Category and sum total
category_sales = df.groupby("Category")["Total"].sum()
print("\n📊 Sales by Category:")
print(category_sales)

# Most sold product by quantity
most_sold = df.loc[df["Quantity"].idxmax()]
print("\n🏆 Most Sold Product:")
print(most_sold["Product"], "-", most_sold["Quantity"], "units")

big_sales = df[df["Total"] > 1000]
print("\n📦 Orders over €1000:\n", big_sales)


sales_by_date = df.groupby("Date")["Total"].sum()
print("\n🗓️ Sales per Day:\n", sales_by_date)

product_sales = df.groupby("Product")["Total"].sum().sort_values(ascending=False)
print("\n🔝 Product Revenue:\n", product_sales)

