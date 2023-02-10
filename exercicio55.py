# Fazer um programa para fornecer a soma dos N primeiros numeros impares positivos

numero_atual = 1
continuar = True
soma = 0

while continuar == True:
    numero = input('Digite quantos números impares positivos deseja somar: ')
    contador = numero
    try:
        contador = int(contador)
        if contador <= 0:
            print('Número inválido.')
        else:
            break
    except:
        print('Número inválido.')
        continue

        continue

while contador > 0:
    soma += numero_atual
    numero_atual += 2
    contador -= 1

print(f'A soma total dos primeiros {numero} números ímpares é: {soma}')
