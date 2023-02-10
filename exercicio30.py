# 30 - Faca um programa que leia 3 numeros e os imprima em ordem decrescente

numero1 = input('Digite o primeiro número: ')
numero2 = input('Digite o segundo número: ')
numero3 = input('Digite o terceiro número: ')

numero1 = int(numero1)
numero2 = int(numero2)
numero3 = int(numero3)

if numero1 <= numero2 and numero2 <= numero3:
    print(f'A ordem decrescente é: {numero3}, {numero2}, {numero1}')
elif numero2 <= numero1 and numero1 <= numero3:
    print(f'A ordem crescente é: {numero3}, {numero1}, {numero2}')
elif numero3 <= numero1 and numero1 <= numero2:
    print(f'A ordem decrescente é: {numero2}, {numero1}, {numero3}')
elif numero1 <= numero3 and numero3 <= numero2:
    print(f'A ordem decrescente é: {numero2}, {numero3}, {numero1}')
elif numero2 <= numero3 and numero3 <= numero1:
    print(f'A ordem decrescente é: {numero1}, {numero3}, {numero2}')
else:
    print(f'A ordem crescente é: {numero1}, {numero2}, {numero3}')
