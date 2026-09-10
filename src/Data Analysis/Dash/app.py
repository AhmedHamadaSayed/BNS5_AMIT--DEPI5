import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output


# Read data
df = pd.read_csv("Dash.csv")


# Create Dash app
app = Dash(__name__)

app.title = "Sales Dashboard"


# Get numeric columns
num_cols = df.select_dtypes(include="number").columns


# Dashboard layout
app.layout = html.Div([

    html.H1("Sales Dashboard"),

    html.Label("Select a value:"),

    dcc.Dropdown(
        id="column-dropdown",
        options=[
            {"label": col, "value": col}
            for col in num_cols
        ],
        value=num_cols[0]
    ),

    dcc.Graph(
        id="pie-chart"
    )

])


# Callback
@app.callback(
    Output("pie-chart", "figure"),
    Input("column-dropdown", "value")
)
def update_pie(selected_col):

    grouped = df.groupby("Area")[selected_col].sum().reset_index()

    fig = px.pie(
        grouped,
        names="Area",
        values=selected_col,
        title=f"Distribution of {selected_col} by Area",
        hole=0.4
    )

    return fig


# Run app
if __name__ == "__main__":
    app.run(debug=True)