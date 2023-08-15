# Importações
import pandas as pd
import plotly.graph_objects as go
import re

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

# Visualização: Proporção por Status
labels = ['Presentes', 'Ausentes', 'Eliminados']
colors = ['lightgreen', 'green', 'darkgreen']
values = [len(df_presentes), len(df_ausentes), len(df_eliminados)]
fig_proporcao_candidatos = go.Figure(data=[go.Pie(labels=labels, values=values, marker=dict(colors=colors))])
fig_proporcao_candidatos.update_layout(
    title='Proporção de candidatos por status',
    plot_bgcolor='#060606',   # Fundo escuro
    paper_bgcolor='#060606',  # Fundo escuro
    font=dict(color='#CCCCCC'))  # Texto cinza claro