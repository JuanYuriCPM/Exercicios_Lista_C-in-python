# 31 - Faca um programa que leia 3 numeros e imprima o valor intermediario entre o maior e o menor

numero1 = input('Digite o primero número: ')
numero2 = input('Digite o segundo número: ')
numero3 = input('Digite o terceiro número: ')

numero1 = int(numero1)
numero2 = int(numero2)
numero3 = int(numero3)

if numero1 <= numero2 and numero3 <= numero1:
    print(f'{numero1} é o valor intermediário')
elif numero1 <= numero3 and numero2 <= numero1:
    print(f'{numero1} é o valor intermediário')
elif numero2 <= numero1 and numero3 <= numero2:
    print(f'{numero2} é o valor intermediário')
elif numero2 <= numero3 and numero1 <= numero2:
    print(f'{numero2} é o valor intermediário')
elif numero3 <= numero1 and numero2 <= numero3:
    print(f'{numero3} é o valor intermediário')
else:
    print(f'{numero3} é o valor intermediário')

    