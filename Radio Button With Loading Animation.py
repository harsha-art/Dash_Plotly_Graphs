from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
def make_graph():
    df = pd.read_csv("time.csv",low_memory=False)
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df.index,
        y=df['Real Time'],
        name='Real Time',
        marker_color='blue'
    ))
    fig.add_trace(go.Bar(
        x=df.index,
        y=df['Scheduled Time'],
        name='Scheduled Time',
        marker_color='green'
    ))

    # Set the layout
    fig.update_layout(
        title='Real Time vs Scheduled Time',
        xaxis=dict(
            tickmode='array',
            tickvals=list(df.index),
            ticktext=list(df.index)
        ),
        xaxis_title='Event',
        yaxis_title='Time',
        barmode='group',
        paper_bgcolor="#222222",
        font_color= "white",
    )
    return fig
dataframe_users = pd.read_csv("bus_travel_dataset.csv", low_memory=False)
dataframe_time = pd.read_csv("time.csv",low_memory=False)
dataframe_hours = pd.read_csv("passtime.csv",low_memory=False)
app = Dash(__name__,external_stylesheets=[dbc.themes.DARKLY])

def make_pie():
    fig = go.Figure()
    fig.add_trace(go.Pie(
            labels=dataframe_users['StopFrom'],
            values=dataframe_users['PassengerCount'],
            titlefont=dict(size=20),
            titleposition='top right',

        ))
    fig.update_layout(
        title="No Of Passengers per stop",
        paper_bgcolor="#222222",
        font_color="white",
    )
    return fig
def make_bar():
    fig = go.Figure()
    fig.add_trace(go.Bar(
             x=dataframe_hours['Time'],
             y=dataframe_hours["Number of Passengers"],
        marker=dict(
            color=dataframe_hours["Number of Passengers"],
            colorscale = "Viridis",
            showscale = True,
        )

         ),
    )
    fig.update_layout(
        xaxis_title="Time of the day",
        yaxis_title="Numbers of Passengers",
        title="No Of Passengers per stop",
        paper_bgcolor="#222222",
        font_color="white",
    )
    return fig
app.layout = dbc.Container(
    [
        html.H3("Select an option"),
        html.P("Select a graph:"),
        dcc.RadioItems(
            id="selection",
            options=[
                {"label": "No Of Users per stop", "value": "No Of Users per stop"},
                {"label": "No Of Users throughtout the day", "value": "No Of Users throughtout the day"},
                {'label':'Scheduled time vs Real Time','value':'Scheduled time vs Real Time'},
            ],
            value="No Of Users per stop"
        ),
        dcc.Loading(
            dcc.Graph(id="graph",style={"background-color": "#f83212"}),
            type="cube"),
    ]
,)


@app.callback(
    Output("graph", "figure"), Input("selection", "value")
)
def display_animated_graph(selection):
    animations = {
        "No Of Users per stop": make_pie(),
         "No Of Users throughtout the day" : make_bar(),
        "Scheduled time vs Real Time": make_graph(),
    }
    return animations[selection]


if __name__ == "__main__":
    app.run_server(debug=True)
