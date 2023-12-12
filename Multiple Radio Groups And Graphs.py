from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

class MakingGraphs():
    def __init__(self,filepath):
        self.filepath = filepath
        self.data = pd.read_csv(filepath)
    def makepie(self,labels,values,title_text):
        fig = go.Figure()
        fig.add_trace(go.Pie(
                labels=self.data[labels],
                values=self.data[values],
                titlefont=dict(size=20),
                titleposition='top right',
            ))
        fig.update_layout(
            title=title_text,
            paper_bgcolor="#222222",
            font_color="white",
            # line=dict(color='#000000', width=2),
        )
        fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
        return fig
    def makepie_crop_prediction(self,state_value,district_value):
        fig = go.Figure()
        data1 = self.data[self.data['State_Name'] == state_value]
        data1 = data1[data1['District_Name'] == district_value]
        fig.add_trace(go.Pie(
                labels=data1['Crop'],
                titlefont=dict(size=20),
                titleposition='top right',
            ))
        fig.update_layout(
            title="Crop Distribution For The District "+ district_value.title(),
            paper_bgcolor="#222222",
            font_color="white",
        )
        fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
        return fig
    def makebar(self,x_val,y_val,title,x_title_text,y_title_text):
        fig = go.Figure()
        fig.add_trace(go.Bar(
                 x=self.data[x_val],
                 y=self.data[y_val],
                 base='group',
            marker=dict(
                color =  'darkolivegreen',
            )

             ),
        )
        fig.update_layout(
            xaxis_title= x_title_text,
            yaxis_title= y_title_text,
            title=title,
            paper_bgcolor="#222222",
            font_color="white",
        )
        return fig
    def make_rainfall_bar(self,markdown_value,title,x_title_text,y_title_text):
        fig = go.Figure()
        data1 = self.data[self.data['SUBDIVISION'] == markdown_value]
        reshaped_data = data1.loc[:, 'JAN':'DEC'].stack().reset_index(level=1)
        reshaped_data.columns = ['Month', 'Rainfall']
        if(markdown_value not in ['ANDAMAN & NICOBAR ISLANDS', 'ARUNACHAL PRADESH', 'ASSAM & MEGHALAYA', 'NAGA MANI MIZO TRIPURA', 'SUB HIMALAYAN WEST BENGAL & SIKKIM', 'GANGETIC WEST BENGAL', 'ORISSA', 'JHARKHAND', 'BIHAR', 'EAST UTTAR PRADESH', 'WEST UTTAR PRADESH', 'UTTARAKHAND', 'HARYANA DELHI & CHANDIGARH', 'PUNJAB', 'HIMACHAL PRADESH', 'JAMMU & KASHMIR', 'WEST RAJASTHAN', 'EAST RAJASTHAN', 'WEST MADHYA PRADESH', 'EAST MADHYA PRADESH', 'GUJARAT REGION', 'SAURASHTRA & KUTCH', 'KONKAN & GOA', 'MADHYA MAHARASHTRA', 'MATATHWADA', 'VIDARBHA', 'CHHATTISGARH', 'COASTAL ANDHRA PRADESH', 'TELANGANA', 'RAYALSEEMA', 'TAMIL NADU', 'COASTAL KARNATAKA', 'NORTH INTERIOR KARNATAKA', 'SOUTH INTERIOR KARNATAKA', 'KERALA', 'LAKSHADWEEP']):
            markdown_value = "Not Selected"
        fig.add_trace(go.Bar(
            x=reshaped_data['Month'],
            y=reshaped_data['Rainfall'],
            base='group',
            marker=dict(
                color =  'coral',
            )

             ),
        )
        fig.update_layout(
            xaxis_title= markdown_value,
            yaxis_title= y_title_text,
            title=title + markdown_value.title(),
            paper_bgcolor="#202422",
            font_color="white",
        )
        return fig
    def make_rainfall_bar(self,markdown_value,title,x_title_text,y_title_text):
        fig = go.Figure()
        data1 = self.data[self.data['SUBDIVISION'] == markdown_value]
        reshaped_data = data1.loc[:, 'JAN':'DEC'].stack().reset_index(level=1)
        reshaped_data.columns = ['Month', 'Rainfall']
        if(markdown_value not in ['ANDAMAN & NICOBAR ISLANDS', 'ARUNACHAL PRADESH', 'ASSAM & MEGHALAYA', 'NAGA MANI MIZO TRIPURA', 'SUB HIMALAYAN WEST BENGAL & SIKKIM', 'GANGETIC WEST BENGAL', 'ORISSA', 'JHARKHAND', 'BIHAR', 'EAST UTTAR PRADESH', 'WEST UTTAR PRADESH', 'UTTARAKHAND', 'HARYANA DELHI & CHANDIGARH', 'PUNJAB', 'HIMACHAL PRADESH', 'JAMMU & KASHMIR', 'WEST RAJASTHAN', 'EAST RAJASTHAN', 'WEST MADHYA PRADESH', 'EAST MADHYA PRADESH', 'GUJARAT REGION', 'SAURASHTRA & KUTCH', 'KONKAN & GOA', 'MADHYA MAHARASHTRA', 'MATATHWADA', 'VIDARBHA', 'CHHATTISGARH', 'COASTAL ANDHRA PRADESH', 'TELANGANA', 'RAYALSEEMA', 'TAMIL NADU', 'COASTAL KARNATAKA', 'NORTH INTERIOR KARNATAKA', 'SOUTH INTERIOR KARNATAKA', 'KERALA', 'LAKSHADWEEP']):
            markdown_value = "Not Selected"
        fig.add_trace(go.Bar(
            x=reshaped_data['Month'],
            y=reshaped_data['Rainfall'],
            base='group',
            marker=dict(
                color =  'coral',
            )

             ),
        )
        fig.update_layout(
            xaxis_title= markdown_value,
            yaxis_title= y_title_text,
            title=title + markdown_value.title(),
            paper_bgcolor="#202422",
            font_color="white",
        )
        return fig
    def makeScatter(self,x_val,y_val,title,x_axis_title):
        fig = go.Figure()
        fig.add_trace(go.Scatter(
                 x=self.data[x_val],
                 text=[f'The Ph Value Is: {x}' for x in self.data[x_val]],
                 mode = "markers", 
                 hoverinfo = 'text',
                 marker=dict(
                    size=10,  
                    color=self.data[x_val],
                    colorscale='Blackbody',  
                    showscale=True
                ),     
             ),
        )
        fig.update_layout(
            title=title,
            xaxis_title= x_axis_title,
            paper_bgcolor="#222222",
            font_color="white",
            font_size = 20,
            xaxis=dict(title=dict(
                font=dict(
                size=23,  
                color="white", 
                )),
            tickfont=dict(
                size=14, 
                color="white", 
                )
            )
        )
        fig.update_xaxes(showgrid=True, gridwidth=2.5, gridcolor='black')
        fig.update_yaxes(showgrid=True, gridwidth=2.5, gridcolor='black')
        return fig
    def make_crop_recommendation_pie(self):
        fig = go.Figure()
        fig.add_trace(go.Pie(
                labels=['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate', 'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee'],
                values=[99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99],
                titlefont=dict(size=20),
                titleposition='top right',
            ))
        fig.update_layout(
            title="Crops Recommended In Dataset",
            paper_bgcolor="#222222",
            font_color="white",
            # line=dict(color='#000000', width=2),
        )
        fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
        return fig

rainfall = MakingGraphs('C:/xampp/htdocs/agriculture-portal-main/farmer/ML/rainfall_prediction/rainfall_in_india_1901-2017.csv')
yield_boi = MakingGraphs('C:/xampp/htdocs/agriculture-portal-main/farmer/ML/yield_prediction/crop_production_karnataka.csv')
crop_recommendation = MakingGraphs('C:/xampp/htdocs/agriculture-portal-main/farmer/ML/crop_recommendation/Crop_recommendation.csv')
crop_prediction = MakingGraphs('C:/xampp/htdocs/agriculture-portal-main/farmer/ML/crop_prediction/preprocessed2.csv')

app = Dash(__name__,external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div(
    [
        html.H3("Select a dataset to visualize".title()),
        html.Div(children=[
            html.H4("Crop Predition Dataset:"),
            dcc.RadioItems(
                id="selection_crop_pred",
                options=[
                    {'label':'Select State In Dropdown','value':'districtpie'},
                ],
            ),
            dcc.Dropdown(
            options = {'Andaman and Nicobar Islands': 'Andaman and Nicobar Islands', 'Andhra Pradesh': 'Andhra Pradesh', 'Arunachal Pradesh': 'Arunachal Pradesh', 'Assam': 'Assam', 'Bihar': 'Bihar', 'Chandigarh': 'Chandigarh', 'Chhattisgarh': 'Chhattisgarh', 'Dadra and Nagar Haveli': 'Dadra and Nagar Haveli', 'Goa': 'Goa', 'Gujarat': 'Gujarat', 'Haryana': 'Haryana', 'Himachal Pradesh': 'Himachal Pradesh', 'Jammu and Kashmir ': 'Jammu and Kashmir ', 'Jharkhand': 'Jharkhand', 'Karnataka': 'Karnataka', 'Kerala': 'Kerala', 'Madhya Pradesh': 'Madhya Pradesh', 'Maharashtra': 'Maharashtra', 'Manipur': 'Manipur', 'Meghalaya': 'Meghalaya', 'Mizoram': 'Mizoram', 'Nagaland': 'Nagaland', 'Odisha': 'Odisha', 'Puducherry': 'Puducherry', 'Punjab': 'Punjab', 'Rajasthan': 'Rajasthan', 'Sikkim': 'Sikkim', 'Tamil Nadu': 'Tamil Nadu', 'Telangana ': 'Telangana ', 'Tripura': 'Tripura', 'Uttar Pradesh': 'Uttar Pradesh', 'Uttarakhand': 'Uttarakhand', 'West Bengal': 'West Bengal'},
            value = 'Andaman and Nicobar Islands', 
            placeholder="Select Your State",
            style={'color': 'tomato', 'font-size': 16},
            id='markdown_value_pred'),
            dcc.Dropdown(
            placeholder="Select Your State For District",
            style={'color': 'tomato', 'font-size': 16},
            id='markdown_value_districs'),
            ],style={'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '3vw', 'margin-top': '3vw'}),
        html.Div(children=[
            html.H4("\nCrop Recommendation Dataset:"),
            dcc.RadioItems(
                id="selection_crop_recommend",
                options=[
                    {"label": "Crop Recommended In Dataset", "value": "Crops_Recommended"},
                    {"label": "Ph Distribution", "value": "PH"},
                ],
            ),], style={'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '3vw', 'margin-top': '3vw'}),
        html.Div(children=[
            html.H4("Rainfall In India Dataset:"),
            dcc.RadioItems(
                id="selection_rain",
                options=[
                    {"label": 'States Represented In Analysis', "value": 'Average Rainfall in Pie Chart'},
                    {"label": 'States Represented In Bar Graph', "value": 'Average Rainfall in Bar Graph'},
                    {'label':'Rainfall Throughtout The Year In','value':'Rainfall Per Month In Each State'},
                ],
            ),
            dcc.Dropdown(
            options = {'ANDAMAN & NICOBAR ISLANDS': 'ANDAMAN & NICOBAR ISLANDS', 'ARUNACHAL PRADESH': 'ARUNACHAL PRADESH', 'ASSAM & MEGHALAYA': 'ASSAM & MEGHALAYA', 'NAGA MANI MIZO TRIPURA': 'NAGA MANI MIZO TRIPURA', 'SUB HIMALAYAN WEST BENGAL & SIKKIM': 'SUB HIMALAYAN WEST BENGAL & SIKKIM', 'GANGETIC WEST BENGAL': 'GANGETIC WEST BENGAL', 'ORISSA': 'ORISSA', 'JHARKHAND': 'JHARKHAND', 'BIHAR': 'BIHAR', 'EAST UTTAR PRADESH': 'EAST UTTAR PRADESH', 'WEST UTTAR PRADESH': 'WEST UTTAR PRADESH', 'UTTARAKHAND': 'UTTARAKHAND', 'HARYANA DELHI & CHANDIGARH': 'HARYANA DELHI & CHANDIGARH', 'PUNJAB': 'PUNJAB', 'HIMACHAL PRADESH': 'HIMACHAL PRADESH', 'JAMMU & KASHMIR': 'JAMMU & KASHMIR', 'WEST RAJASTHAN': 'WEST RAJASTHAN', 'EAST RAJASTHAN': 'EAST RAJASTHAN', 'WEST MADHYA PRADESH': 'WEST MADHYA PRADESH', 'EAST MADHYA PRADESH': 'EAST MADHYA PRADESH', 'GUJARAT REGION': 'GUJARAT REGION', 'SAURASHTRA & KUTCH': 'SAURASHTRA & KUTCH', 'KONKAN & GOA': 'KONKAN & GOA', 'MADHYA MAHARASHTRA': 'MADHYA MAHARASHTRA', 'MATATHWADA': 'MATATHWADA', 'VIDARBHA': 'VIDARBHA', 'CHHATTISGARH': 'CHHATTISGARH', 'COASTAL ANDHRA PRADESH': 'COASTAL ANDHRA PRADESH', 'TELANGANA': 'TELANGANA', 'RAYALSEEMA': 'RAYALSEEMA', 'TAMIL NADU': 'TAMIL NADU', 'COASTAL KARNATAKA': 'COASTAL KARNATAKA', 'NORTH INTERIOR KARNATAKA': 'NORTH INTERIOR KARNATAKA', 'SOUTH INTERIOR KARNATAKA': 'SOUTH INTERIOR KARNATAKA', 'KERALA': 'KERALA', 'LAKSHADWEEP': 'LAKSHADWEEP'}, 
            value = 'LAKSHADWEEP', 
            placeholder="Select Your Location",
            style={'color': 'tomato', 'font-size': 16},
            id='state_dropdown'),
            ],style={'display':'inline-block','vertical-align':'top','margin-top':'3vw','margin-left':'3vw'}, className='row'),
        html.Div(children=[
            html.Div(children=[
                html.H4("\nYield Prediction Dataset:"),
                dcc.RadioItems(
                    id="selection_yield",
                    options=[
                        {"label": "District Names", "value": "District_Names"},
                    ],
                    ),
                ], style={'margin-left': '3vw', 'margin-top': '3vw'}),],className="row"),
        dcc.Loading([
            dcc.Graph(id="graph1",style={"background-color": "#f83212"})],
            type="cube",id="loading-graph1"),
        dcc.Loading([
            dcc.Graph(id="graph2",style={"background-color": "#f83212"})],
            type="cube", id="loading-graph2"),
         dcc.Loading([
            dcc.Graph(id="graph3",style={"background-color": "#f83212"})],
            type="cube", id="loading-graph3"),
         dcc.Loading([
            dcc.Graph(id="graph4",style={"background-color": "#f83212"})],
            type="cube", id="loading-graph4"),
    ],style={"backgroundColor": "#222222"} )

@app.callback(
    Output('markdown_value_districs','options'),
    Input('markdown_value_pred','value'))
def display_districts(value):
    a = crop_prediction.data[crop_prediction.data['State_Name'] == value]
    a = a['District_Name']
    dic = {}
    for x in a:
        if x not in dic:
            dic[x] = x
    return dic

@app.callback(
    Output("graph1","figure"),
    Input("selection_crop_pred","value"),
    Input("markdown_value_pred","value"),
    Input('markdown_value_districs','value'),)
def display_graph_crop_pred(value,markdown_val_crop_pred,district_name):
    print(value,markdown_val_crop_pred)
    animations = {
        'districtpie': crop_prediction.makepie_crop_prediction(markdown_val_crop_pred,district_name)
    }
    return animations[value]

@app.callback(
    Output("graph2", "figure"), 
    Input("selection_crop_recommend", "value"),
)
def display_graph_crop_recommend(value):
    print(value)
    animations = {
        'Crops_Recommended': crop_recommendation.make_crop_recommendation_pie(),
        "PH":crop_recommendation.makeScatter("ph","ph","Distribution Of PH Values","PH Values In Dataset")
    }
    return animations[value]
@app.callback(
    Output("graph3", "figure"), 
    Input("selection_rain", "value"),
    Input("state_dropdown","value"),
)
def display_graph_rainfall(value,markdown_val_rainfall):
    print(value)
    animations = {
        'Average Rainfall in Pie Chart': rainfall.makepie('SUBDIVISION','ANNUAL',"All The State Values in the graph"),
        'Average Rainfall in Bar Graph': rainfall.makebar('SUBDIVISION','ANNUAL','States represented in Bar Graph','State','Annual Rainfall(in mm)'),
        'Rainfall Per Month In Each State': rainfall.make_rainfall_bar(markdown_val_rainfall,'Rainfall In ','ANDAMAN & NICOBAR ISLANDS','Annual Rainfall'),
        }
    return animations[value]
@app.callback(
    Output("graph4", "figure"), 
    Input("selection_yield", "value"),
)
def display_graph_yield(value):
    animations = {
        'District_Names': yield_boi.makepie("District_Name","Production","Production Per District"),
    }
    return animations[value]


if __name__ == "__main__":
    app.run_server(port=1111)