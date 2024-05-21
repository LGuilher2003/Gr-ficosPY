import pandas as pd
import plotly.express as px
df = pd.read_excel('Dados.xlsx', sheet_name='Dados Cadastrais', nrows=351)
values = df['Turma']
names = df['Idade -Cálculo média']
fig = px.pie(df,values=values,names=names,title='Média de idade das turmas')
fig.update_traces(
            textposition ='inside',
            textinfo = 'percent+label'
)
fig.show( )