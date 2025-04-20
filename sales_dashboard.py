import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Use a clean visual theme
sns.set_theme(style="whitegrid")

# Load and prepare data
df = pd.read_csv("sales.csv")
df["Total"] = df["Quantity"] * df["Price"]

# Create figure and subplots
plt.figure(figsize=(15, 5))

# 1. Sales by Product (Bar)
plt.subplot(1, 3, 1)
sns.barplot(data=df, x="Product", y="Total", estimator=sum, ci=None)
plt.title("💰 Total Sales by Product")
plt.xticks(rotation=45)

# 2. Sales Over Time (Line)
plt.subplot(1, 3, 2)
sns.lineplot(data=df, x="Date", y="Total", estimator=sum, ci=None, marker="o")
plt.title("📈 Daily Sales Over Time")
plt.xticks(rotation=45)

# 3. Sales by Category (Pie - uses Matplotlib only)
plt.subplot(1, 3, 3)
category_sales = df.groupby("Category")["Total"].sum()
plt.pie(category_sales, labels=category_sales.index, autopct="%1.1f%%", startangle=140)
plt.title("🥧 Sales by Category")

plt.tight_layout()
plt.show()
