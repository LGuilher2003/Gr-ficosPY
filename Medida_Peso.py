import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Dados.xlsx', sheet_name='Medidas antropométricas', nrows=351)
df = df[['Estatura', 'Peso', 'IMC', 'Envergadura']]

Media_Estatura = df['Estatura'].mean()
Media_Peso = df['Peso'].mean()
Media_Imc = df['IMC'].mean()
Media_Envergadura = df['Envergadura'].mean()

medias = pd.DataFrame({
    'Medida': ['Estatura', 'Peso', 'IMC', 'Envergadura'],
    'Média': [Media_Estatura, Media_Peso, Media_Imc, Media_Envergadura]
})
for i, value in enumerate(medias['Média']):
    plt.text(i, value + 0.02 * value, f'{value:.2f}', ha='center', va='bottom')

plt.bar(medias['Medida'], medias['Média'], color=['blue', 'green', 'red', 'purple'])

plt.title('Média das Medidas Antropométricas')
plt.xlabel('Medidas')
plt.ylabel('Média')


plt.show()
