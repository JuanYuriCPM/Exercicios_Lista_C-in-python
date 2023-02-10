# 27 - Faca um programa que leia 2 numeros e os imprima em ordem crescente

numero1 = input('Digite o primeiro número: ')
numero2 = input('Digite o segundo número: ')

if numero1 > numero2:
    print(f'A ordem crescente é: {numero2}, {numero1}')
else:
    print(f'A ordem crescente é: {numero1}, {numero2}')