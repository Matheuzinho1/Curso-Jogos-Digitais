#UTLIZANDO O SEGUINTE SITE PARA EXECUÇÃO DOS CÓDIGOS: https://jupyter.org/try-jupyter
#BIBLIOTECA PANDAS USADA PARA TRABALHAR COM MANIPULAÇÃO DE DADOS
import pandas as pd

data = {'Nome':['Alice','Bob','Juliano'],
'Idade':[20,15,17],
'Bairro':['Penha','Cangaiba','Tatuapé']
}
df = pd.DataFrame(data)
print(df)

#BIBLIOTECA MATPLOTLIB USADA PARA REALIZAR GRAFICOS
import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,4,9,7])
plt.show()

#TABUADA NORMAL COM FUNÇÃO
def tabuada(x):
    n = 0
    while n< = 10:
        print(n , " x ", x , " = ", n*x)
        n = n + 1
tabuada(7)

#UTILIZAÇÃO DA BIBLIOTECA PANDAS E MATPLOTLIB JUNTAS
import pandas as pd
dados = {
    'Categoria':['A','B','C','D'],
    'Valor':[14,20,5,14]
}
df = pd.DataFrame(dados)
df.plot(kind='pie', y='Valor', labels=df['Categoria'], autopct='%1.1f%%', startangle=90)
plt.show()