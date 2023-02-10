# 20 - Entrar com um numero e informar se ele e ou nao divisivel por 5

numero = input('Digite o número a ser analisado: ')

numero = int(numero)

if numero % 5 == 0:
    print('O número digitado é divisível por 5')
else:
    print('O número digitado não é divisível por 5') 