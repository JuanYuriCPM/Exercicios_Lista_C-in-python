# Faca um programa que leia 12 numeros e imprima a media desses numeros

contador = 12
soma = 0

while contador > 0:
    
    numero_atual = input('Digite um número: ')

    try:
        numero_atual = int(numero_atual)
    except:
        print('Número inválido.')
        continue

    soma += numero_atual
    contador -= 1

print('A média total dos números é: ', soma/12)    