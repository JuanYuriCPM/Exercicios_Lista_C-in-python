"""
Faca um programa que leia um valor e chame uma funcao para calcular e exibir o fatorial deste valor
"""

def calculo_fatorial(numero):
    total = numero
    for i in alcance:
        total *= i
    print(f'\nO valor de {numero} fatorial é: {total}\n')

while True:
    numero = input('Digite um número para se calcular o fatorial: ')
    try:
        numero = int(numero)
    except:
        print('\nInput inválido, por favor digite apenas números positivos inteiros.\n')
        continue
    
    if numero < 0:
        print('\nNúmero inválido, por favor digite apenas números positivos inteiros.\n')
        continue
    elif numero == 0:
        print('\nO valor de 0 fatorial é: 1\n')
        continue
    alcance = range(1, numero)
    calculo_fatorial(numero)