import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load and prepare data
df = pd.read_csv("sales.csv")
df["Total"] = df["Quantity"] * df["Price"]

# Barplot: Total sales per product
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Product", y="Total", estimator=sum, ci=None)
plt.title("💰 Total Sales by Product")
plt.ylabel("Total Sales (€)")
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 4))
sns.lineplot(data=df, x="Date", y="Total", estimator=sum, ci=None)
plt.title("📈 Sales Over Time")
plt.show()


plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x="Category", y="Price")
plt.title("💡 Price Distribution by Category")
plt.show()


plt.figure(figsize=(5, 4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("🔬 Correlation Matrix")
plt.show()
