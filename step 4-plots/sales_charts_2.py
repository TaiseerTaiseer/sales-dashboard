import pandas as pd
import matplotlib.pyplot as plt

# Load the sales data
df = pd.read_csv("sales.csv")

# Add a total sales column
df["Total"] = df["Quantity"] * df["Price"]

# Group by Date and sum total sales
daily_sales = df.groupby("Date")["Total"].sum()

# Plot line chart
daily_sales.plot(kind="line", marker='o', title="📈 Daily Sales Over Time")
plt.ylabel("Total Sales (€)")
plt.xlabel("Date")
plt.grid(True)
plt.tight_layout()
plt.show()
