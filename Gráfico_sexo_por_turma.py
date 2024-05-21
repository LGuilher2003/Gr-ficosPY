import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_excel('Dados.xlsx', sheet_name='Dados Cadastrais', nrows=351)
df = df[['Nome', 'Sexo', 'Turma', 'Idade -Cálculo média']]

sexo_por_turma = df.groupby(['Turma', 'Sexo']).size().reset_index(name='Count')

df.plot(kind="bar")
fig = px.bar(sexo_por_turma, x='Turma', y='Count', color='Sexo', title='Distribuição de Sexo por Turma',barmode='group',
             color_discrete_map={'F': 'pink', 'M': 'blue'})
fig.show()
