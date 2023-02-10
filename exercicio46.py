# Faca um programa que leia 20 numeros e exiba a soma desses numeros

contador = 20
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

print('A soma total dos números é: ', soma)    