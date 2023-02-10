""" 60 - Fazer um programa para mostrar o S dado por: 

S = 1/N + 2/(N-1) + 3/(N-2) + .... N / (N - (N-1)) """



while True:
    numero = input('Digite um número: ')
    try:
        numero = int(numero)
        if numero <= 0:
            print('Número inválido.')
            continue
        break
    except:
        print('Número inválido.')
        continue

alcance = range(0,numero+1,1)
total = 0


for valor in alcance:
    total = total + valor/(numero - (valor-1))


print(total)


