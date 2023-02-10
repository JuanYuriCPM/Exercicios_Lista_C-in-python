# 19 - Faca um programa que leia um numero e imprima uma mensagem dizendo se e par ou impar

numero = input('Digite o número a ser analisado: ')

numero = int(numero)

if numero % 2 == 0:
    print('O número digitado é par')
else: 
    print('O número digitado é impar')