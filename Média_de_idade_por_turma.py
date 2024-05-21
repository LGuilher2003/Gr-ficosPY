import pandas as pd
import plotly.express as px

df = pd.read_excel('Dados.xlsx', sheet_name='Dados Cadastrais', nrows=351)


idade_por_turma = df.groupby(['Turma', 'Idade -Cálculo média']).size().reset_index(name='Count')

for turma in idade_por_turma['Turma'].unique():
    turma_df = idade_por_turma[idade_por_turma['Turma'] == turma]
    fig = px.pie(turma_df, 
                 values='Count', 
                 names='Idade -Cálculo média', 
                 title=f'Proporção das Idades na Turma {turma}')
    fig.update_traces(
        textposition='inside',
        textinfo='percent+label'
    )
    fig.show()
