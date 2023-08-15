# Importações
import pandas as pd
import plotly.graph_objects as go
import re
from functions import functions

# Carregamento dos Dados
def load_data(path):
    """Carrega o dataset do caminho especificado."""
    return pd.read_csv(path, encoding="utf8", sep=',')

df = load_data("Dados_ENEM_Reduzido.csv")

# Funções de Preprocessamento
def filter_presentes(df):
    """Filtra os alunos presentes em todas as provas."""
    return df[(df["TP_PRESENCA_CN"] == 1) &
              (df["TP_PRESENCA_CH"] == 1) &
              (df["TP_PRESENCA_LC"] == 1) &
              (df["TP_PRESENCA_MT"] == 1)].reset_index(drop=True)

def filter_ausentes(df):
    """Filtra os alunos ausentes em ao menos uma das provas e não eliminados."""
    return df[((df["TP_PRESENCA_CN"] == 0) |
               (df["TP_PRESENCA_CH"] == 0) |
               (df["TP_PRESENCA_LC"] == 0) |
               (df["TP_PRESENCA_MT"] == 0)) &
              ~((df["TP_PRESENCA_CN"] == 2) |
                (df["TP_PRESENCA_CH"] == 2) |
                (df["TP_PRESENCA_LC"] == 2) |
                (df["TP_PRESENCA_MT"] == 2))]

def filter_eliminados(df):
    """Filtra os alunos ausentes em ao menos uma das provas e não eliminados."""
    return df[(df["TP_PRESENCA_CN"] == 2) |
        (df["TP_PRESENCA_CH"] == 2) |
        (df["TP_PRESENCA_LC"] == 2) |
        (df["TP_PRESENCA_MT"] == 2)]

def compute_mean_scores(df):
    """Calcula a média das notas para cada aluno e adiciona à DataFrame."""
    df_notas = df[['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']].copy()
    df["Média"] = df_notas.mean(axis=1)
    return df

# Análises e Visualizações

## Análise: Proporção por Status
df_presentes = filter_presentes(df)
df_ausentes = filter_ausentes(df)
df_eliminados = filter_eliminados(df)

## Análise: Média das Notas por Cor/Raça
df_presentes = compute_mean_scores(df_presentes)
cor_raca_dict = {
    0: 'Não declarado',
    1: 'Branca',
    2: 'Preta',
    3: 'Parda',
    4: 'Amarela',
    5: 'Indígena',
    6: 'Não dispõe da informação'
}
grouped = df_presentes.groupby('TP_COR_RACA')['Média'].mean()
labels = [cor_raca_dict[codigo] for codigo in grouped.index]

# Cosntrução do gráfico
fig_medianotas_corraca = functions.bar_graph(labels, grouped.values, title='Média das Notas por Etnia', range=[450, 600])

## Análise: Média das Notas por Sexo
media_por_sexo = df_presentes.groupby('TP_SEXO')[['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']].mean()
notas = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']
areas = {
    'NU_NOTA_CN': 'CN',
    'NU_NOTA_CH': 'CH',
    'NU_NOTA_LC': 'LC',
    'NU_NOTA_MT': 'MT',
    'NU_NOTA_REDACAO': 'RD'
}
sexos = ['Feminino', 'Masculino']
cores = ['#006400', '#008000', '#228B22', '#32CD32', '#90EE90']

fig_medianotas_sexo = go.Figure()
for nota, cor in zip(notas, cores):
    fig_medianotas_sexo.add_trace(go.Bar(
        x=sexos,
        y=media_por_sexo[nota],
        name=areas[nota],
        marker_color=cor
    ))
fig_medianotas_sexo.update_layout(title="Média das Notas por Sexo dos Alunos", title_x=0.5,
                                    plot_bgcolor='#060606',   # Fundo escuro
                                    paper_bgcolor='#060606',  # Fundo escuro
                                    font=dict(color='#CCCCCC'),  # Texto cinza claro                                   
                                    #xaxis_title="Sexo",
                                    #yaxis_title="Média das Notas",
                                    yaxis=dict(range=[500, 600]),
                                    barmode='group')

# Análise relacionada ao tipo de escola e sua média
escola_mapping = {
    1: 'Não Respondeu',
    2: 'Pública',
    3: 'Privada',
    4: 'Exterior'
}
df_presentes['TP_ESCOLA_NOME'] = df_presentes['TP_ESCOLA'].map(escola_mapping)
mean_scores_by_school_type = df_presentes.groupby('TP_ESCOLA_NOME')['Média'].mean()

# Construção do gráfico média das notas por tipo de escola
fig_tipoescola_media = functions.bar_graph(mean_scores_by_school_type.index,
                                        mean_scores_by_school_type.values, 
                                        title="Média das Notas por Tipo de Escola",
                                        range=[500, 600])

# Análise de Correlações entre Notas
matriz_correlacao = df[["NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "NU_NOTA_REDACAO"]].corr()
labels = ["CM", "CH", "LC", "MT", "RD"]

# Construção do gráfico de correlações
fig_correlacao_notas = functions.heatmap_graph(    
    labels,
    labels,
    matriz_correlacao,
    title="Correlações entre as Notas do ENEM"
)

# Análise de Renda Média vs Média das Notas
income_mapping = {
    'A': 0,
    'B': 1212 / 2,
    'C': (1212.01 + 1818) / 2,
    'D': (1818.01 + 2424) / 2,
    'E': (2424.01 + 3030) / 2,
    'F': (3030.01 + 3636) / 2,
    'G': (3636.01 + 4848) / 2,
    'H': (4848.01 + 6060) / 2,
    'I': (6060.01 + 7272) / 2,
    'J': (7272.01 + 8484) / 2,
    'K': (8484.01 + 9696) / 2,
    'L': (9696.01 + 10908) / 2,
    'M': (10908.01 + 12120) / 2,
    'N': (12120.01 + 14544) / 2,
    'O': (14544.01 + 18180) / 2,
    'P': (18180.01 + 24240) / 2,
    'Q': 24240 + (24240 * 0.25)  # considerando a faixa Q como 25% acima do limite inferior
}
df_presentes['Q006'] = df_presentes['Q006'].map(income_mapping)

# Análise de Renda Média vs Média das Notas Agrupado
grouped = df_presentes.groupby("Média")['Q006'].mean().reset_index()
fig_rendamedia_notasagrupada = functions.scatter_graph(
    grouped['Q006'],
    grouped["Média"],
    title='Renda Média vs Média das Notas Agrupada')