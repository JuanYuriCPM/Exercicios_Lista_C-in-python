# 28 -Faca um programa que leia 3 numeros e imprima o menor deles

numero1 = input('Digite o primeiro número: ')
numero1 = int(numero1)

menor_atual = numero1

numero2 = input('Digite o segundo número: ')
numero2 = int(numero2)

if numero2 < menor_atual:
    menor_atual = numero2

numero3 = input('Digite o terceiro número: ')
numero3 = int(numero3)

if numero3 < menor_atual:
    menor_atual = numero3

print(f'O menor número é: {menor_atual}')