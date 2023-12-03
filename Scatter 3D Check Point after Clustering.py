from dash import Dash, dcc, html, Output, Input, callback
import plotly.express as px
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline


attributes = ["Age", "Gender", "BCLOT", "A/G RAT", "TBIL", "TGLO", "TREP", "ALB", "GGT", "SGOT", "SGPT", "ALKPO4"]
abnormal = pd.read_csv("abnormal.csv", low_memory=False, nrows=25000, usecols=attributes)

num_clusters = 6
kmeans = KMeans(n_clusters=num_clusters, init='k-means++', random_state=42).fit(abnormal)

abnormal['Cluster'] = kmeans.labels_  # Add the 'Cluster' column to the DataFrame

scaler = StandardScaler()
pca = PCA(n_components=3)

preprocessing_pipeline = Pipeline([
    ('scaler', scaler),
    ('pca', pca)
])

pca_data = preprocessing_pipeline.fit_transform(abnormal)
pca_df = pd.DataFrame(pca_data, columns=[f"PC{i+1}" for i in range(3)])

cluster_labels = abnormal['Cluster']
pc1, pc2, pc3 = pca_df['PC1'], pca_df['PC2'], pca_df['PC3']

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])


app.layout = html.Div([
    html.H1('Enter the Value'),
    dcc.Input(
        id="mytext",
        type="text",
        placeholder="Enter the text",
        debounce=True,
        value=""
    ),
    dcc.Graph(id="graph", figure={}),
])


@app.callback(
    Output(component_id='graph', component_property='figure'),
    Input(component_id="mytext", component_property="value")
)
def update_text(chosen_val):
    if chosen_val == "":
        cluster_labels_str = cluster_labels.astype(str)
        fig = px.scatter_3d(pca_df, x=pc1, y=pc2, z=pc3, color= cluster_labels_str,
                            title="Clusters",opacity=0.8,hover_data={'cluster':cluster_labels})
    else:
        input_list = chosen_val.split(",")
        val = {
            "Age": [input_list[0]], "Gender": [input_list[1]], "BCLOT": [input_list[2]],
            "A/G RAT": [input_list[3]], "TBIL": [input_list[4]], "TGLO": [input_list[5]],
            "TREP": [input_list[6]], "ALB": [input_list[7]], "GGT": [input_list[8]],
            "SGOT": [input_list[9]], "SGPT": [input_list[10]], "ALKPO4": [input_list[11]],
        }

        new_data_point = pd.DataFrame(val)
        new_data_point.loc[new_data_point['Gender'] == 'M', 'Gender'] = 1
        new_data_point.loc[new_data_point['Gender'] == 'F', 'Gender'] = 0
        from sklearn.preprocessing import StandardScaler
        from sklearn.decomposition import PCA

        # Assuming you have your original dataset loaded into a pandas DataFrame called 'data'
        # Assuming you have a new data point stored in a pandas DataFrame called 'new_data_point'

        # Select only the numerical columns for preprocessing
        numerical_columns = ['Age', 'Gender', 'BCLOT', 'A/G RAT', 'TBIL', 'TGLO', 'TREP', 'ALB', 'GGT', 'SGOT', 'SGPT',
                             'ALKPO4']

        # Extract the numerical data from the original dataset
        numerical_data = abnormal[numerical_columns]

        # Preprocess the numerical data by scaling
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(numerical_data)

        # Fit PCA on the scaled data
        pca = PCA(n_components=3)
        pca.fit(scaled_data)

        # Preprocess the new data point by scaling
        new_data_point_scaled = scaler.transform(new_data_point[numerical_columns])

        # Transform the new data point using the fitted PCA model
        new_data_point_transformed = pca.transform(new_data_point_scaled)

        # Extract the values of PCA1, PCA2, and PCA3 for the new data point
        pca1_value = new_data_point_transformed[0, 0]
        pca2_value = new_data_point_transformed[0, 1]
        pca3_value = new_data_point_transformed[0, 2]

        # Print the values of PCA1, PCA2, and PCA3
        print("PCA1:", pca1_value)
        print("PCA2:", pca2_value)
        print("PCA3:", pca3_value)
        # fig.add_trace(go.Scatter(x=df1["Age"], y=df1["BCLOT"], marker_symbol='x', marker_size=10000 ))
        cluster_labels_str = cluster_labels.astype(str)
        new_row = {'PC1': [pca1_value], 'PC2': [pca2_value], 'PC3': [pca3_value]}
        fig = px.scatter_3d(pca_df, x=pc1, y=pc2, z=pc3, color=cluster_labels_str,
                            title="Clusters", opacity=0.9, hover_data={'cluster': cluster_labels})
        trace = go.Scatter3d(x=new_row['PC1'],
                             y=new_row['PC2'],
                             z=new_row['PC3'],
                             mode='markers',
                             marker=dict(symbol='x', size=10, color= (78,91,100)),
                             name='Selected Points')
        print(new_row)

        # Add the trace to the main scatter plot
        fig.add_trace(trace)

    return fig


if __name__ == '__main__':
    app.run(debug=True)
