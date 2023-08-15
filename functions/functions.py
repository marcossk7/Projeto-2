import plotly.graph_objects as go
# Função para gráfico de Barras
args=[
'#060606', # Fundo escuro
'#060606', # Fundo escuro
dict(color='#CCCCCC') # Texto cinza claro
]  

def bar_graph(eixo_x, eixo_y, color: str ='green', title: str =None, xtitle: str =None, ytitle: str =None, range: list =None, args=args):
    fig = go.Figure(data=[go.Bar(
        x=eixo_x,
        y=eixo_y,
        marker_color=color
    )])

    fig.update_layout(        
        plot_bgcolor=args[0],  
        paper_bgcolor=args[1], 
        font=args[2],  
        title_text=title, title_x=0.5,
        xaxis_title=xtitle,
        yaxis_title=ytitle,
        yaxis = dict(
            showgrid=True,
            gridcolor='gray',
            gridwidth=0.5,
            range=range,
        )        
    )
    return fig

# Função para gráfico de Pizza

def pie_graph(labels, values, marker=dict(colors=['lightgreen', 'green', 'darkgreen']), title=None, args=args):
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        marker=marker
    )])

    fig.update_layout(        
        plot_bgcolor=args[0],   
        paper_bgcolor=args[1],  
        font=args[2],  
        title_text=title, title_x=0.5      
    )
    return fig

# Função para gráfico de Distribuição

def scatter_graph(eixo_x, eixo_y, colorscale='Greens', mode='markers', title=None, xtitle=None, ytitle=None, args=args):
    fig = go.Figure(data=[go.Scatter(
        x=eixo_x,
        y=eixo_y,
        mode=mode,
        marker=dict(
            size=10,
            color=eixo_y,
            colorscale=colorscale,
            showscale=True
    )
    )])

    fig.update_layout(        
        plot_bgcolor=args[0],   
        paper_bgcolor=args[1], 
        font=args[2],  
        title_text=title, title_x=0.5,
        xaxis_title=xtitle,
        yaxis_title=ytitle
        )        
    return fig

# Função para gráfico de Distribuição

def heatmap_graph(eixo_x, eixo_y, eixo_z, colorscale='Greens', title=None, xtitle=None, ytitle=None, args=args):
    fig = go.Figure(data=[go.Heatmap(
        x=eixo_x,
        y=eixo_y,
        z=eixo_z,
        hoverongaps=False,
        colorscale=colorscale
    )])

    fig.update_layout(        
        plot_bgcolor=args[0], 
        paper_bgcolor=args[1], 
        font=args[2],
        title=title, title_x=0.5,
        xaxis=dict(title=xtitle),
        yaxis=dict(title=ytitle)
        )        
    return fig