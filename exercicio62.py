"""Fazer um programa para calcular os N primeiros termos da serie de Taylor 

S = 1 + 1/2 - 1/3 + 1/4 - 1/5 ... 1/N"""


atual = 1
anterior = 0
sinal = 1



while True:
    numero = input('Digite quantos números da série de Taylor deseja exibir: ')
    try:
        numero = int(numero)
        if numero <= 0:
            print('Número inválido.')
            continue
        else:
            break
    except:
        print('Número inválido.')
        continue

alcance = range(1,numero,1)

for i in alcance:
    print(atual)
    atual = sinal * (1/(i + 1))
    sinal *= -1
    