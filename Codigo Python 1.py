num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

num1 = int(num1)  
num2 = int(num2)

res = num1 + num2

if res > 0:
    print("Numero positivo")
else:
    print("Numero negativo")

print("A soma é: ", res)

print("---------------------------")

numeros = 1, -2, 10, -3, -100   
    
for negativo in numeros:
    if negativo < 0:
        print('Negativo')
    else:
        print('Positivo')
        
print("---------------------------")

def minha_lista = []

while True:
    dado = input("Digite um valor (ou 'sair' para encerrar): ")
    if dado.lower() == 'sair':
        break
    else:
        minha_lista.append(dado)

print("Lista final:", minha_lista)
