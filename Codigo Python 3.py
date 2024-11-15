#------------------------
opcao = 's'
while opcao =='s':
    aluno = input('Nome do aluno: ')
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    nota3 = int(input('Nota 3: '))
    nota4 = int(input('Nota 4: '))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media >= 7:
       print("Parabens ",aluno, "Você foi aprovado com a media ",media)
    else:
       print("Infelizmente ",aluno, "Você nao atingiu a media")

    opcao = input("Deseja continuar? (Digite S para Sim / N para Não)")
#------------------------
#------------------------
a = 20

while a >= 0:     
    print("Python, ", a)
    a = a - 1

print("Fim")
#------------------------
#------------------------
def exibir():
    print("Aula - Python")
    print("São Paulo - 24-10-24")
    print("ETEC - Belém")
    print("Feito pelo aluno Matheus")

exibir()
print("Fim desta execução")
#------------------------
#------------------------
def somar(valor1, valor2):
    soma = valor1 + valor2
    print(soma)

preco1 = int(input("Digite Preco1: "))
preco2 = int(input("Digite Preco2: "))    

somar(preco1, preco2)

print("Fim desta execução")
#------------------------
#------------------------
import datetime
agora = datetime.datetime.now()

print(agora)
#------------------------
#------------------------
import datetime
from datetime import date

agora = datetime.datetime.now()
print(agora)
print('-----------------')

data_atual = date.today()
print(data_atual)
print('-----------------')

data_em_texto = data_atual.strftime('%d/%m/%Y')
print(data_em_texto)
#------------------------
#------------------------
import random
valor = random.randint(1, 100)
print("numero", valor)
print("================================================")
print("=== Olá, esse jogo  solicita que você digite ===")
print("== um número de 1 a 100, sendo que o objetivo ==")
print("===== é você  acertar com  o menor  numero  ====")
print("===========    de vezes possíveis     ==========")
print("================================================")

nvezes = int(input("Deseja tentar com quantas tentativas ? "))

while nvezes > 0:
    print("------------------------------------")
    print("Você tem ", nvezes, " tentativas!")
    n = int(input("Escolha um numero de 1 a 100 ? "))
    
    if n == valor:
        print("Parabéns, você acertou! O número é ", valor)
        break
    elif n > valor:
        print("Você escolheu um número muito acima.")
    elif n < valor:
        print("Você escolheu um número muito abaixo.")
    
    nvezes -= 1
    
    if nvezes == 0:
        print("Esgotou o número de tentativas - GAME OVER")
        
print("Fim de programa!")
#------------------------