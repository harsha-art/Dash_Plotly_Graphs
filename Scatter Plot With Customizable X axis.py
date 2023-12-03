from dash import Dash, dcc, html, Output, Input, callback
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

dataframe = pd.read_csv(r"C:\Users\shars\Downloads\abnormal.csv",low_memory=False)
#print(dataframe.shape)


app.layout = dbc.Container([

    dbc.Row(
        dbc.Col(html.H1("Enter The X Axis Column Here",
                        className='text-center text-white mb-4'),
                width=12)
    ),

    dbc.Row([

        dbc.Col([
            dcc.Input(
                id="mytext",
                type="text",
                placeholder="Enter the text",
                debounce=True,
                value="",
                style={
                    'height': '50px',
                    'width': '1200px',
                    'font-size': "100%",
                    'min-height': '1px',
                }
            )
        ],width={'size':12, 'offset':0, 'order':1},
        ),

        dbc.Col([
            dcc.Graph(id='graph', figure={})
        ], width={'size':12, 'offset':0, 'order':2},
        ),

    ], justify='around'),  # Horizontal:start,center,end,between,around
], fluid=True)



@app.callback(
    Output(component_id='graph', component_property='figure'),
    Input(component_id="mytext", component_property="value")
)
def update_text(chosen_val):
    print(chosen_val)
    if chosen_val == "":
        fig = px.scatter(dataframe, x='SGOT', y='BCLOT',color='BCLOT',
                         hover_name=dataframe.index,size_max=65)
    else:
        fig = px.scatter()
        fig = px.scatter(dataframe, x=chosen_val, y='BCLOT',color='Age',
                         hover_name=dataframe.index,size_max=65)

    return fig


if __name__ == '__main__':
    app.run(debug=True)
