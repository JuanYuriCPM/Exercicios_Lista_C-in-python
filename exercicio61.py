# 61 - Fazer um programa para mostrar os N primeiros termos da serie de FIBONACCI: 1,1,2,3,5,8,13,21,... 


valor_atual = 1
valor_anterior = 0
soma = 1

while True:
    numero = input('Digite quantos números da sequência fibonnaci deseja exibir: ')
    try:
        numero = int(numero)
        if numero <= 0:
            print('Número inválido.')
            continue
        else:
            break
    except:
        print('Número inválido')
        continue

alcance = range(0,numero,1)

for i in alcance:
    print(soma)
    soma = valor_atual + valor_anterior
    valor_anterior = valor_atual
    valor_atual = soma


