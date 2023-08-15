from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from apps_análises import averages_analysis

layout = dbc.Container([ 
    html.Div([  # Adicione esta Div ao início do seu layout
    dcc.Link('Voltar para a página principal', href='/'),
    html.Br(),  # Isso é apenas para dar algum espaço entre o link e o resto do conteúdo
    ], #style={'height': '2vh', 'margin-top': '0.25vh'}
    ),
    html.H4(['Análise da Média das Notas dos Participantes'], style={'text-align' : 'center', 'margin-top': '10px'}),
    dbc.Row([
        
        dbc.Col([
            dcc.Graph(
            id='fig_medianotas_corraca',
            figure=averages_analysis.fig_medianotas_corraca,
            style={'height': '30vh', 'margin-top': '0.5vh'}
            ),
            dcc.Graph(
            id='fig_medianotas_sexo',
            figure=averages_analysis.fig_medianotas_sexo,
            style={'height': '30vh', 'margin-top': '0.5vh'}
            ),                        
        ], width=6),
        dbc.Col([
            dcc.Graph(
            id='fig_tipoescola_media',
            figure=averages_analysis.fig_tipoescola_media,
            style={'height': '30vh', 'margin-top': '0.5vh'}
            ),
            dcc.Graph(
            id='fig_correlacao_notas',
            figure=averages_analysis.fig_correlacao_notas,
            style={'height': '30vh', 'margin-top': '0.5vh'}
            ),             
        ], width=6)  
    ]),
    dbc.Row([        
        dbc.Col([  # Adicione um dbc.Col para manter a consistência
            dcc.Graph(
                id='fig_rendamedia_notasagrupada',
                figure=averages_analysis.fig_rendamedia_notasagrupada,
                style={'height': '36vh', 'margin-top': '0.25vh'}
            ),
        ], width=12)
    ])
], fluid=True #, style={'width': '794px', 'margin': '0 auto'}
)