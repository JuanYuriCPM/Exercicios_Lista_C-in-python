# 11 - Faça um programa que leia do teclado uma temperatura em graus Celsius e faça a conversão para Fahrenheit, imprimindo o resultado.

celsius = input('Digite o valor da temperatura em Celsius:')

celsius = int(celsius)
fahrenheit = (1.8 * celsius) + 32

print(f'{celsius} graus Celsius equivalem a: {fahrenheit:.2f} graus Fahrenheit')