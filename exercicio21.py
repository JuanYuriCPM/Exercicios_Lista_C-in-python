# 21 - Entrar com um numero e informar se ele e ou nao divisivel por 3 e 7

numero = input('Digite o número a ser analisado: ')

numero = int(numero)

if numero % 3 == 0 and numero % 7 == 0:
    print('O número digitado é divisível por 3 e 7')
else:
    print('O número digitado não é divisível por 3 e 7')