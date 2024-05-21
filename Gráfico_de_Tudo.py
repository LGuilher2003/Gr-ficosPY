import pandas as pd
import matplotlib.pyplot as plt
tabela = pd.read_excel('Dados.xlsx', sheet_name='Medidas antropométricas', nrows=350)
tabela = tabela[['Nome','IMC','Peso','Estatura']]


tabela['IMC'] = tabela['IMC'].replace(r'^\s*$', 'NaN', regex=True)


tabela['IMC'] = pd.to_numeric(tabela['IMC'], errors='coerce').fillna(0)
tabela['Peso'] = pd.to_numeric(tabela['Peso'], errors='coerce').fillna(0)
tabela['Estatura'] = pd.to_numeric(tabela['Estatura'], errors='coerce').fillna(0)


tabela.set_index('Nome', inplace=True)

tabela.plot(kind ='bar')
plt.xlabel('Nome')
plt.ylabel('IMC')
plt.ylabel('Peso')
plt.ylabel('Estatura')
plt.title('IMC por Nome')
plt.xticks(rotation=  60)
plt.show()