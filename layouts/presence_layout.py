from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from apps_análises import presence_analysis

layout = dbc.Container([
    dbc.Row([
        html.Div([  # Adicione esta Div ao início do seu layout
        dcc.Link('Voltar para a página principal', href='/'),
        html.Br(),  # Isso é apenas para dar algum espaço entre o link e o resto do conteúdo
        ]),
        dbc.Col([
            dcc.Graph(
            id='fig-prop-candidatos',
            figure=presence_analysis.fig_proporcao_candidatos               
            )                            
        ], width=6),
        dbc.Col([
            
        ], width=6)  
    ]),
    dbc.Row([
        dbc.Col([
            
        ], width=6),
        dbc.Col([
            
        ], width=6)  
    ])
], fluid=True)