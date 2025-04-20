import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("sales.csv")

# Add a total sales column
df["Total"] = df["Quantity"] * df["Price"]

# Group by product and sum total sales
product_sales = df.groupby("Product")["Total"].sum()

# Plot bar chart
product_sales.plot(kind="bar", title="💰 Sales by Product")
plt.ylabel("Total Sales (€)")
plt.xlabel("Product")
plt.tight_layout()
plt.show()
