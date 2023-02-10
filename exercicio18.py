# 18 - Faca um programa para ler dois numeros e efetua a adicao desses dois numeros.Caso a soma seja maior ou igual a 10, mostre esses numeros.

numero1 = input('Digite o primeiro número: ')
numero2 = input('Digite o segundo número: ')

numero1 = int(numero1)
numero2 = int(numero2)
soma = numero1 + numero2

if soma >= 10:
    print('A soma é: ', soma)
else:
    print('A soma não é maior ou igual a 10')