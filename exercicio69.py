"""
Faca um programa para ler uma quantidade e chamar uma funcao que imprima os termos da serie de fibonacci para este valor
"""

def calculo_fibonacci(numero):
    valor_atual = 1
    valor_anterior = 0
    soma = 1
    alcance = range(0,numero,1)
    for i in alcance:
        print(soma)
        soma = valor_atual + valor_anterior
        valor_anterior = valor_atual
        valor_atual = soma

while True:
    numero = input('Digite quantos números da sequência fibonnaci deseja exibir: ')
    try:
        numero = int(numero)
        if numero <= 0:
            print('Número inválido.')
            continue
        else:
            break
    except:
        print('Número inválido')
        continue

calculo_fibonacci(numero)