import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px


url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv'
spacex_df = pd.read_csv(url)

max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

my_font = 'verdana' #'Arial' # 'monospace', 'menlo'
my_font_s = 24
# my_font_c = '#503D36'

app = Dash(__name__)
app.layout = html.Div([
    html.H1(
        'SpaceX Launch Records Dashboard',
        style={
            'textAlign':'center',
            'color':'#503D36',
            'font-size':40,
            'font-family':my_font
        }
    ),
    html.Br(),
    dcc.Dropdown(
        id='site-dropdown',
        placeholder='Select a Launch Site here',
        options=[
            {'label':'All Sites', 'value':'ALL'},
            {'label':'CCAFS LC-40', 'value':'CCAFS LC-40'},
            {'label':'VAFB SLC-4E', 'value':'VAFB SLC-4E'},
            {'label':'KSC LC-39A', 'value':'KSC LC-39A'},
            {'label':'CCAFS SLC-40', 'value':'CCAFS SLC-40'}
        ],
        value='ALL',
        searchable=True,
        style={
            'font-family':my_font
        }
    ),
    html.Br(),
    html.Div(
        dcc.Graph(
            id='success-pie-chart',
            config={'displayModeBar':False}
        )
    ),
    html.Br(),
    html.P(
        'Payload range (Kg):',
        style={
            'font-family':my_font,
            'font-size':16,
        }
    ),
    html.Br(),
    html.Div(
        dcc.RangeSlider(
            id='payload-slider',
            min=0,
            max=10000,
            # step=1000,
            value=[min_payload, max_payload]
        ),
        style={
            'font-family':my_font
        }
    ),
    html.Div(
        dcc.Graph(
            id='success-payload-scatter-chart',
            config={'displayModeBar':False}
        )
    )
])

@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def update_pie_chart(launch_site):
    if launch_site == 'ALL':
        pie_data = spacex_df.groupby('Launch Site')['class'].sum().reset_index()
        fig = px.pie(
                data_frame=pie_data,
                values='class',  
                names='Launch Site',
                color='Launch Site',
                title='Distribution of successful launches by launch site',
            )
    else:
        pie_data = spacex_df[spacex_df['Launch Site'] == launch_site]['class'].value_counts().reset_index()
        pie_data['class'] = ['success' if cl == 1 else 'fail' for cl in pie_data['class']]
        fig = px.pie(
            data_frame=pie_data,
            values='count',  
            names='class',
            color='class',
            color_discrete_map={'fail':'#EF553B', 'success':'#00CC96'},
            category_orders={'class':['success', 'fail']},
            title=f'All launches for location: {launch_site}',
    )
    fig.update_layout(
        font_family=my_font
    )
    return fig

@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
    Input(component_id='payload-slider', component_property='value')]
)
def update_scatter_chart(launch_site, payload):
    mask_1 = (spacex_df['Payload Mass (kg)'] > payload[0]) & (spacex_df['Payload Mass (kg)'] < payload[1])
    if launch_site == 'ALL':
        scatter_data = spacex_df[mask_1]
    else:
        mask_2 = spacex_df['Launch Site'] == launch_site
        scatter_data = spacex_df[mask_1 & mask_2]
    fig = px.scatter(
        data_frame=scatter_data,
        x='Payload Mass (kg)',
        y='class',
        color='Booster Version Category'
    )
    fig.update_yaxes(tickvals=[0, 1], ticktext=['fail', 'success'])
    return fig


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='7860', debug=True)