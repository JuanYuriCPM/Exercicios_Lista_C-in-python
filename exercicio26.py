# 26 - Faca um programa que leia 2 numeros e os imprima em ordem decrescente

numero1 = input('Digite o primeiro número: ')
numero2 = input('Digite o segundo número: ')

if numero1 > numero2:
    print(f'Os números digitados, em ordem decrescente, são: {numero1}, {numero2}')
else:
    print(f'Os números digitados, em ordem decrescente, são: {numero2}, {numero1}')

