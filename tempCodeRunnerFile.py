import pandas as pd
import plotly.express as px

df = pd.read_excel('Dados.xlsx', sheet_name='Dados Cadastrais', nrows=351)

idade_counts = df['Idade -Cálculo média'].value_counts().reset_index()
idade_counts.columns = ['Idade', 'Count']

fig = px.pie(idade_counts, values='Count', names='Idade', title='Média Total das Idades',color_discrete_map={'11': 'pink', '12': 'blue','13':'red'})
fig.update_traces(
    textposition='inside',
    textinfo='percent+label'
)
fig.show()
