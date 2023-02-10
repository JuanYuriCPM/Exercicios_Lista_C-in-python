#  Faca um programa que leia 10 numeros e imprima a metade de cada numero

contador = 10

while contador > 0:
    numero_atual = input(f'Digite um número: ')
    try:
        numero_atual = int(numero_atual)
    except:
        print('Número inválido.')
        continue

    print(f'A metade de {numero_atual} é: {numero_atual/2}')
    contador -= 1