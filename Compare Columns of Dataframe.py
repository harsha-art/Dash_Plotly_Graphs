import pandas as pd
import dash
from dash.dependencies import Input, Output
from dash import html,dcc
import dash_bootstrap_components as dbc

import plotly.express as px
df = pd.read_csv("abnormal.csv",low_memory=False)

app = dash.Dash(__name__,external_stylesheets=([dbc.themes.SIMPLEX]))
app.layout = html.Div([

        html.Div([
            dcc.Markdown(children= "# Compare Colums Of The Dataset",
            style={"text-align": "center", "font-size":"100%", "color":"black"})]),

        html.Div([
            html.Label(['X-axis categories to compare:'],style={'font-weight': 'bold'}),
            dcc.RadioItems(
                id='xaxis_raditem',
                options=[
                        {'label': 'Age', 'value': 'Age'},
                        {'label': 'Gender', 'value': 'Gender'},
                        {'label': 'BCLOT', 'value': 'BCLOT'},
                        {'label': 'A/G RAT', 'value': 'A/G RAT'},
                        {'label': 'DBIL', 'value': 'DBIL'},
                        {'label': 'IBIL', 'value': 'IBIL'},
                        {'label': 'TBIL', 'value': 'TBIL'},
                        {'label': 'TGLO', 'value': 'TGLO'},
                        {'label': 'TREP', 'value': 'TREP'},
                        {'label': 'ALB', 'value': 'ALB'},
                        {'label': 'GGT', 'value': 'GGT'},
                        {'label': 'SGOT', 'value': 'SGOT'},
                        {'label': 'SGPT', 'value': 'SGPT'},
                        {'label': 'ALKP04', 'value': 'ALKPO4'},
                ],
                value='Age',
                inline=True,
                style={"width": "50%"}
            ),
        ]),

        html.Div([
            html.Br(),
            html.Label(['Y-axis values to compare:'], style={'font-weight': 'bold'}),
            dcc.RadioItems(
                id='yaxis_raditem',
                options=[
                    {'label': 'Age', 'value': 'Age'},
                    {'label': 'Gender', 'value': 'Gender'},
                    {'label': 'BCLOT', 'value': 'BCLOT'},
                    {'label': 'A/G RAT', 'value': 'A/G RAT'},
                    {'label': 'DBIL', 'value': 'DBIL'},
                    {'label': 'IBIL', 'value': 'IBIL'},
                    {'label': 'TBIL', 'value': 'TBIL'},
                    {'label': 'TGLO', 'value': 'TGLO'},
                    {'label': 'TREP', 'value': 'TREP'},
                    {'label': 'ALB', 'value': 'ALB'},
                    {'label': 'GGT', 'value': 'GGT'},
                    {'label': 'SGOT', 'value': 'SGOT'},
                    {'label': 'SGPT', 'value': 'SGPT'},
                    {'label': 'ALKP04', 'value': 'ALKPO4'},
                ],
                value='Gender',
                inline=True,
                style={"width": "50%"}
            ),
        ]),

    html.Div([
        dcc.Graph(id='the_graph')
    ]),

])
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='xaxis_raditem', component_property='value'),
     Input(component_id='yaxis_raditem', component_property='value')]
)

def update_graph(x_axis, y_axis):
    dff = df
    print(dff[[x_axis,y_axis]][:1])

    barchart=px.scatter(
            data_frame=dff,
            x=x_axis,
            y=y_axis,
            title=y_axis+': by '+x_axis,
            )
    barchart.update_layout(xaxis={'categoryorder':'total ascending'},
                           title={'xanchor':'center', 'yanchor': 'top', 'y':0.9,'x':0.5,})

    return (barchart)

if __name__ == '__main__':
    app.run_server(port=3000)
