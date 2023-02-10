# 6 - Faça um programa que leia um número de entrada e imprima o seu antecessor e o seu sucessor

numero = input('Digite o número a ser analisado: ')

numero = int(numero)
antecessor = numero - 1
sucessor = numero + 1

print(f'O antecessor de {numero} é: {antecessor} e seu sucessor é: {sucessor}')