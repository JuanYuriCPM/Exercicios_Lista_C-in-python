# 24 - Faca um programa que leia 3 numeros e imprima uma mensagem dizendo se correspondem aos lados de um triangulo

lado1 = input('Digite o primeiro lado: ')
lado2 = input('Digite o segundo lado: ')
lado3 = input('Digite o terceiro lado: ')

lado1 = int(lado1)
lado2 = int(lado2)
lado3 = int(lado3)

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    print('Os lados informados formam um triângulo.')
else:
    print('Os lados informados não formam um triângulo.')