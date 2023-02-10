# Entrar com 15 numeros e imprimir a quantidade de numeros maiores que 30 que foram digitados

contador = 15
maior_que_15 = 0

while contador > 0:
    numero = input('Digite um número: ')
    try:
        numero = int(numero)
    except:
        print('Número inválido.')
        continue

    if numero > 30:
        maior_que_15 += 1

    contador -= 1

print(f'A quantidade de números maiores que 30 que foram digitados é: {maior_que_15}')