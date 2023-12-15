from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

def make_graph():
    merchent_1 = pd.DataFrame({
        'Values':[19679,19944,18524,9122,7738,9153,8799,9506,10652,13452,9357,4816,4859,5266,7921],
        # 'Merchant':['Merchent 1', 'Merchent 1', 'Merchent 1', 'Merchent 1', 'Merchent 1', 'Merchent 1', 'Merchent 1', 'Merchent 1', 'Merchent 1', 'Merchent 1', 'Merchent 1', 'Merchent 1', 'Merchent 1', 'Merchent 1', 'Merchent 1']
        })
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=['4/14/2016', '4/14/2016', '4/15/2016', '4/15/2016', '4/16/2016', '4/16/2016', '4/17/2016', '4/17/2016', '4/18/2016', '4/18/2016', '4/19/2016', '4/19/2016', '4/20/2016', '4/20/2016', '4/21/2016', '4/21/2016', '4/22/2016', '4/22/2016', '4/23/2016', '4/23/2016', '4/24/2016', '4/24/2016', '4/25/2016', '4/25/2016', '4/26/2016', '4/26/2016', '4/27/2016', '4/27/2016', '4/28/2016', '4/28/2016'],
        y=merchent_1['Values'],
        name="Merchent_1",
        marker_color='blue'
    ))
    merchent_2 = pd.DataFrame({
        'Values': [475,25659,25116,23585,24351,24840,25621,25076,24120,25917,26236,27692,27518,27943,0],
        # 'Merchent':['Merchent 2', 'Merchent 2', 'Merchent 2', 'Merchent 2', 'Merchent 2', 'Merchent 2', 'Merchent 2', 'Merchent 2', 'Merchent 2', 'Merchent 2', 'Merchent 2', 'Merchent 2', 'Merchent 2', 'Merchent 2', 'Merchent 2']
    })
    fig.add_trace(go.Bar(
        x=['4/14/2016', '4/14/2016', '4/15/2016', '4/15/2016', '4/16/2016', '4/16/2016', '4/17/2016', '4/17/2016', '4/18/2016', '4/18/2016', '4/19/2016', '4/19/2016', '4/20/2016', '4/20/2016', '4/21/2016', '4/21/2016', '4/22/2016', '4/22/2016', '4/23/2016', '4/23/2016', '4/24/2016', '4/24/2016', '4/25/2016', '4/25/2016', '4/26/2016', '4/26/2016', '4/27/2016', '4/27/2016', '4/28/2016', '4/28/2016'],
        y=merchent_2['Values'],
        name='Merchent_2',
        marker_color='green'
    ))
    fig.update_layout(
        title='Merchent_1 vs Merchent_2',
        barmode='group',
        paper_bgcolor="#222222",
        font_color= "white",
    )
    return fig

app = Dash(__name__,external_stylesheets=[dbc.themes.DARKLY])
data = pd.read_csv(r"C:\Users\shars\Downloads\juspay.csv")

values = [20154, 45603, 43640, 32707, 32089, 33993, 34420, 34582, 34772, 39369, 35593, 32508, 32377, 33209, 7921]
dates = ['4/14/2016', '4/15/2016', '4/16/2016', '4/17/2016', '4/18/2016', '4/19/2016', '4/20/2016', '4/21/2016', '4/22/2016', '4/23/2016', '4/24/2016', '4/25/2016', '4/26/2016', '4/27/2016', '4/28/2016']

# Create a DataFrame
df = pd.DataFrame({'Date': dates, 'Total Transactions': values})

value_bank = [236,267,248]
bankies = ['Bank 1','Bank 2','Bank 3']

banks_df = pd.DataFrame({'Banks':bankies,'values':value_bank})


value_agg = [53,257, 124, 88, 37]
aggs = ['Agg1','Agg2', 'Agg3', 'Agg4', 'Agg5']

agg_df = pd.DataFrame({'aggs':aggs,'values':value_agg})


success_rate = [74, 85, 85]
banks = ['Bank 1', 'Bank 3', 'Bank 2']
failure_rate = [81, 79, 87]

bank_success = pd.DataFrame({'success': success_rate,'banks':banks})
bank_failure = pd.DataFrame({'failure':failure_rate,'banks':banks})

mer_success_rate = [145,99]
mer = ['Merchent_1',"Merchent_2"]
mer_failure_rate = [119,128]

mer_success = pd.DataFrame({'success': mer_success_rate,'mer':mer})
mer_failure = pd.DataFrame({'failure':mer_failure_rate,'mer':mer})

agg = ['Agg2', 'Agg3', 'Agg4', 'Agg5', 'Agg1']
agg_succ_rate = [86, 43, 30, 15, 23]
agg_fail_rate = [85,39,30,17,14]

agg_succ = pd.DataFrame({'success':agg_succ_rate,'agg':agg})
agg_fail = pd.DataFrame({'fail':agg_fail_rate,'agg':agg})

succ_agg_bank = "[('Bank 1', 'Agg2'), ('Bank 3', 'Agg3'), ('Bank 2', 'Agg3'), ('Bank 3', 'Agg2'), ('Bank 2', 'Agg2'), ('Bank 3', 'Agg4'), ('Bank 3', 'Agg5'), ('Bank 1', 'Agg3'), ('Bank 2', 'Agg4'), ('Bank 2', 'Agg5'), ('Bank 1', 'Agg5'), ('Bank 1', 'Agg1'), ('Bank 2', 'Agg1'), ('Bank 3', 'Agg1'), ('Bank 1', 'Agg4')]"
fail_agg_bank = " [('Bank 2', 'Agg2'), ('Bank 1', 'Agg5'), ('Bank 1', 'Agg2'), ('Bank 1', 'Agg3'), ('Bank 2', 'Agg4'), ('Bank 3', 'Agg2'), ('Bank 3', 'Agg4'), ('Bank 2', 'Agg5'), ('Bank 2', 'Agg3'), ('Bank 3', 'Agg3'), ('Bank 1', 'Agg1'), ('Bank 2', 'Agg1'), ('Bank 3', 'Agg1'), ('Bank 3', 'Agg5')]"
app.layout = html.Div(
    [
    dcc.Loading([
        dcc.Graph(id="graph1",figure=px.bar(data, y='Total Transactions',x='Merchant'),style={"background-color": "#f83212"})],
        type="cube",id="loading-graph1"),
    dcc.Loading([
        dcc.Graph(id="graph2",figure=px.bar(df,y='Total Transactions',x='Date'),style={"background-color": "#f83212"})],
        type="cube", id="loading-graph2"),
    dcc.Loading([
        dcc.Graph(id="graph",figure=px.bar(banks_df,y='values',x='Banks'),style={"background-color": "#f83212"})],
        type="cube", id="loading-graph"),
    dcc.Loading([
        dcc.Graph(id="gr2aph",figure=px.bar(agg_df,y='values',x='aggs'),style={"background-color": "#f83212"})],
        type="cube", id="loadin2g-graph"),
    html.H3("Bank Success Rate".title()),
     dcc.Loading([
       dcc.Graph(id="graph3",figure = px.bar(bank_success,x='banks',y='success'), style={"background-color": "#f83212"})],
        type="cube", id="loading-graph3"),
    html.H3("Bank failure rate"),
     dcc.Loading([
        dcc.Graph(id="graph4",figure = px.bar(bank_failure,x='banks',y='failure'),style={"background-color": "#f83212"})],
        type="cube", id="loading-graph4"),
    html.H3("Merchant Success Rate".title()),
     dcc.Loading([
       dcc.Graph(id="graph380",figure = px.bar(mer_success,x='mer',y='success'), style={"background-color": "#f83212"})],
        type="cube", id="loading-graph3"),
    html.H3("Merchant failure rate"),
     dcc.Loading([
        dcc.Graph(id="graph4",figure = px.bar(mer_failure,x='mer',y='failure'),style={"background-color": "#f83212"})],
        type="cube", id="loading-graph4"),
    html.H3("Augg Success Rate".title()),
     dcc.Loading([
       dcc.Graph(id="graph3180",figure = px.bar(agg_succ,x='agg',y='success'), style={"background-color": "#f83212"})],
        type="cube", id="loading-graph213"),
    html.H3("Augg failure rate"),
     dcc.Loading([
        dcc.Graph(id="graph4432",figure = px.bar(agg_fail,x='agg',y='fail'),style={"background-color": "#f83212"})],
        type="cube", id="loading-graph431"),  
     dcc.Loading([
        dcc.Graph(id="graph5",figure = make_graph(),style={"background-color": "#f83212"})],
        type="cube", id="loading-graph5"),  
    html.H1('The Successful agg and bank combination is Bank 1, Agg4'),
    html.H1('The Success trans are 244 and the failed ones are 247'), 
    html.H6(f"All Successful Agg Banks is {succ_agg_bank}".title()), 
    html.H6(f"All Fail Agg Banks is {fail_agg_bank}".title()),


     ],style={"backgroundColor": "#222222"} )
if __name__ == "__main__":
    app.run_server(port=1111)