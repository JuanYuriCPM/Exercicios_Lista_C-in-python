# 7 - Faça um programa que leia dois números e exiba a soma desses números e a diferença entre eles

numero1 = input('Digite o primeiro número: ')
numero2 = input('Digite o segundo número: ')

numero1 = int(numero1)
numero2 = int(numero2)
soma = numero1 + numero2
diferenca = numero1 - numero2

if diferenca < 0:
    diferenca = diferenca * (-1)

print(f'A soma dos dois números é de: {soma} e a diferença é de: {diferenca}')