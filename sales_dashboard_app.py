import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Load your sales data
df = pd.read_csv("sales.csv")
df["Total"] = df["Quantity"] * df["Price"]

# Create Dash app
app = dash.Dash(__name__)

# Layout with dropdown and graph
app.layout = html.Div([
    html.H1("📊 Sales Dashboard", style={'textAlign': 'center'}),
    
    html.Label("Select a Product:"),
    dcc.Dropdown(
        id='product-dropdown',
        options=[{"label": p, "value": p} for p in df["Product"].unique()],
        value=df["Product"].unique()[0],  # default selection
        clearable=False
    ),
    
    dcc.Graph(id='sales-graph')
])

# Callback to update chart
@app.callback(
    Output('sales-graph', 'figure'),
    Input('product-dropdown', 'value')
)
def update_graph(selected_product):
    filtered_df = df[df["Product"] == selected_product]
    daily_sales = filtered_df.groupby("Date")["Total"].sum().reset_index()
    
    fig = px.line(
        daily_sales,
        x="Date",
        y="Total",
        markers=True,
        title=f"📈 Daily Sales for {selected_product}"
    )
    return fig

# Run app
app = dash.Dash(__name__)
server = app.server  # Optional but safe

# layout and callbacks go here...

# ✅ DO NOT include: if __name__ == "__main__"
# ✅ DO NOT include: app.run()







