# 5 - Faça um programa que leia dois numeros de entrada e imprima o resto da divisão inteira de um pelo outro

numero1 = input('Digite o primeiro número: ')
numero2 = input('Digite o segundo número: ')

numero1 = int(numero1)
numero2 = int(numero2)
resto = numero1 % numero2

print(f'O resto da divisão de {numero1} por {numero2} é de: {resto:.2f}')