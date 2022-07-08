import dash
from dash import dcc
from dash import html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input
from plotly.subplots import make_subplots

data = pd.read_csv('https://raw.githubusercontent.com/hwwbg/DECIS-DataScientist/main/inflationanalysis.csv')
data.sort_values("year", inplace=True)

app = dash.Dash(__name__)

server = app.server
app.title = "Inflation Sensitive Analysis for SSA"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Img(src='https://upload.wikimedia.org/wikipedia/commons/8/87/The_World_Bank_logo.svg'),
                html.H1(children="Inflation Sensitive Analysis",),
                html.P(children="Porject the poverty under the shock of inflation",),
            ],
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Country"),
                        dcc.Dropdown(
                            id="country-filter",
                            options=[
                                {"label": countrycode, "value": countrycode}
                                for countrycode in np.sort(data.countrycode.unique())
                            ],
                            value="MWI",
                            clearable=False,
                            searchable=False,
                        ),
                    ],
                ),
            ],
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="poverty-chart",
                        config={"displayModeBar": False},
                    ),
                ),
                html.Div(
                    children=dcc.Graph(
                        id="gini-chart",
                        config={"displayModeBar": False},
                    ),
                ),
            ],
        ),
    ]
)


@app.callback(
    [Output("poverty-chart", "figure"), Output("gini-chart", "figure")],
    [Input("country-filter", "value"),],
)

def update_charts(countrycode):
    mask = (data.countrycode == countrycode)
    filtered_data = data.loc[mask, :]
    
    poverty_chart_figure = make_subplots(rows=1,cols=1,shared_xaxes=True)
    poverty_chart_figure.append_trace(
        {
            'x':filtered_data["year"],
            'y':filtered_data["povS1"],
            'type':'scatter',
            'name':'Food inf>Nonfood inf',
            'hovertemplate': '%{y:.2f}%<extra></extra>',
        },
   1,1)
    poverty_chart_figure.append_trace(
        {
            'x':filtered_data["year"],
            'y':filtered_data["povS2"],
            'type':'scatter',
            'name':'Food inf<Nonfood inf',
            'hovertemplate': '%{y:.2f}%<extra></extra>',
        },
    1,1)
    poverty_chart_figure.append_trace(
        {
            'x':filtered_data["year"],
            'y':filtered_data["povS3"],
            'type':'scatter',
            'name':'Distribution neutral(post-war)',
            'hovertemplate': '%{y:.2f}%<extra></extra>',
        },
    1,1)
    poverty_chart_figure.append_trace(
        {
            'x':filtered_data["year"],
            'y':filtered_data["povS5"],
            'type':'scatter',
            'name':'Distribution neutral(pre-war)',
            'hovertemplate': '%{y:.2f}%<extra></extra>',
        },
    1,1) 
    poverty_chart_figure.update_layout(title_text="Poverty projection",xaxis_tickformat='d')
    
    gini_chart_figure = make_subplots(rows=1, cols=1,shared_xaxes=True)
    gini_chart_figure.append_trace(
        {
            'x':filtered_data["year"],
            'y':filtered_data["giniS1"],
            'type':'scatter',
            'name':'Food inf>Nonfood inf',
            'hovertemplate': '%{y:.2f}%<extra></extra>',
        },
   1,1)
    gini_chart_figure.append_trace(
        {
            'x':filtered_data["year"],
            'y':filtered_data["giniS2"],
            'type':'scatter',
            'name':'Food inf<Nonfood inf',
            'hovertemplate': '%{y:.2f}%<extra></extra>',
        },
    1,1)
    gini_chart_figure.append_trace(
        {
            'x':filtered_data["year"],
            'y':filtered_data["giniS3"],
            'type':'scatter',
            'name':'Distribution neutral(post-war)',
            'hovertemplate': '%{y:.2f}%<extra></extra>',
        },
    1,1)
    gini_chart_figure.append_trace(
        {
            'x':filtered_data["year"],
            'y':filtered_data["giniS5"],
            'type':'scatter',
            'name':'Distribution neutral(pre-war)',
            'hovertemplate': '%{y:.2f}%<extra></extra>',
        },
    1,1)
    gini_chart_figure.update_layout(title_text="Gini Index projection",xaxis_tickformat='d')
    return poverty_chart_figure, gini_chart_figure


if __name__ == "__main__":
    app.run_server(debug=False)
