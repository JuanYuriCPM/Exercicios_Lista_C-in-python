# Entrar com dois numeros e imprimir todos os inteiros no intervalo entre o menor e o maior

continuar1 = True
continuar2 = True

while continuar1 is True:
    numero1 = input('Digite um número: ')
    try:
        numero1 = int(numero1)
        continuar1 = False
    except:
        print('Número inválido.')
        continue

while continuar2 is True:
    numero2 = input('Digite o segundo número: ')
    try:
        numero2 = int(numero2)
        continuar2 = False
    except:
        print('Número inválido.')
        continue

if numero1 <= numero2:
    numero_menor = numero1
    numero_maior = numero2
else:
    numero_menor = numero2
    numero_maior = numero1

numeros = range(numero_menor+1, numero_maior, 1)

if numero_maior - numero_menor <= 1:
    print('Não há números inteiros no intervalo entre os números escolhidos.')
else:
    print('O intervalo entre os números digitados é:')
    for numero in numeros:
        print(numero)