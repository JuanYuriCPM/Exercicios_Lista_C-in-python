# 22 - Entrar com um numero e informar se ele e divisivel por 10, ou e divisivel por 5 ou e divisivel por 2 ou se nao e divisivel por nenhum deles

numero = input('Digite o número a ser analisado: ')

numero = int(numero)

if numero % 10 == 0:
    print('O número digitado é divisível por 10')
else:
    print('O número digitado não é divisível por 10')

if numero % 5 == 0:
    print('O número digitado é divisível por 5')
else:
    print('O número digitado não é divisível por 5')

if numero % 2 == 0:
    print('O número digitado é divisível por 2')
else:
    print('O número digitado não é divisível por 2')

if numero % 10 != 0 and numero % 5 != 0 and numero %2 != 0:
    print('O número digitado não é divisível por 10, 5 ou 2')