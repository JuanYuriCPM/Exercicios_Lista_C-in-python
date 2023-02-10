# 32 - Faca um programa que leia 3 numeros e imprima uma das seguintes mensagens: Todos os numeros sao iguais, Todos os numeros sao diferentes, Apenas dois numeros sao iguais

numero1 = input('Digite o primero número: ')
numero2 = input('Digite o segundo número: ')
numero3 = input('Digite o terceiro número: ')

numero1 = int(numero1)
numero2 = int(numero2)
numero3 = int(numero3)

if numero1 == numero2 == numero3:
    print('Todos os números são iguais')
elif numero1 != numero2 != numero3:
    print('Todos os números são diferentes')
else:
    print('Apenas dois números são iguais')