from dash import Dash, dcc, html, Output, Input, callback
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

dataframe = pd.read_csv("abnormal.csv",low_memory=False)
#print(dataframe.shape)


app.layout = dbc.Container([

    dbc.Row(
        dbc.Col(html.H1("Machine Learning Stuff Idk Tbh ",
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
        fig = px.scatter(dataframe, x='Age', y='BCLOT',size='Age',color='BCLOT',
                         hover_name=dataframe.index,size_max=65)
    else:
        input_list = chosen_val.split(",")
        print(input_list)
        val = {
            "Age": [input_list[0]], "Gender": [input_list[1]], "BCLOT": [input_list[2]], "A / G": [input_list[3]],
            "RAT": [input_list[4]], "DBIL": [input_list[5]], 'IBIL': [input_list[6]], 'TBIL': [input_list[7]],
            "TREP": [input_list[8]], "ALB": [input_list[9]], "GGT": [input_list[10]], "SGOT": [input_list[11]],
            "SGPT": [input_list[12]], "ALKP04": [input_list[13]]
        }
        df1 = pd.DataFrame(val)
        fig = px.scatter(dataframe, x='Age', y='BCLOT',size='BCLOT',color='Age',
                         hover_name=dataframe.index,size_max=65)
        fig.add_trace(go.Scatter(x=df1["Age"], y=df1["BCLOT"], marker_symbol='x', marker_size=100 ))

    return fig


if __name__ == '__main__':
    app.run(debug=True)
