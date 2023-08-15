from dash import Dash, dcc, html, Input, Output
from app import app
from apps_análises import presence_analysis, averages_analysis
from layouts import presence_layout, averages_layout

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/presence_analysis':
        return presence_layout.layout
    elif pathname == '/apps/averages_analysis':
        return averages_layout.layout
    else:
        # Pode adicionar outras rotas ou uma página inicial aqui
        return html.Div([
            html.H2("Indíce", style={'margin-top' : '10px', 'font-size' : '80px'}),
            html.Br(),
            dcc.Link(html.B(['Análise da Presença dos Participantes']), 
                    href='/apps/presence_analysis', 
                    style={'margin-top' : '10px', 'font-size' : '20px'}),
            html.Br(),
            dcc.Link(html.B(['Análise da Média das Notas dos Participantes']), 
                    href='/apps/averages_analysis',
                    style={'margin-top' : '10px', 'font-size' : '20px'}),
            # Adicione links para outras páginas aqui
        ], style={
            'display': 'flex',
            'flexDirection': 'column',
            'alignItems': 'center'}
        )
    

if __name__ == '__main__':
    app.run_server(debug=False)