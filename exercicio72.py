"""
Faca um programa que exiba um menu com as opcoes das seguintes funcoes matematicas:

- par(x)
- resto(x,y)
- max(x,y)
- abs(x)
- exp(x,y)

O menu deve ser exibido ate que o usuario digite ESC para sair
"""
def try_int(numero):
    try:
        numero = int(numero)
        return numero
    except:
        numero = input('Input inválido.Por favor digitar um número inteiro: ')
        return numero

def calculo_par(x):
        if x % 2 == 0:
            print('O número digitado é par.\n')
            return x
        if x %2 != 0:
            print('O número digitado não é par.\n')
            return x

def calculo_resto(x, y):
    print(f'O resto de {x} dividido por {y} é: {x % y}\n')

def calculo_maximo(x, y):
    print(f'O valor max ({x},{y}) é: {(x + y + abs(x-y))/2}\n')

def calculo_absoluto(x):
    print(f'O valor absoluto de {x} é: {abs(x)}\n')

def calculo_exponencial(x, y):
    print(f'O número {x} elevado a {y} é igual a: {x**y}\n')

    


escolhas = ['1', '2', '3', '4', '5', 'ESC']

while True:
    escolha = input('Menu:\n\n1 - Par (x)\n2 - Resto (x, y)\n3 - Máximo (x, y)\n4 - Absoluto (x)\n5 - Exponencial (x, y)\nESC - Sair\n\nDigite uma opção: ')
    while escolha not in escolhas:
        escolha = input('Opção inválida, por favor digite uma opção válida: ')
    if escolha == '1':
        x = input('Digite um valor para verificar se é par: ')
        while type(x) != int:
            x = try_int(x)
        x = calculo_par(x)
    if escolha == '2':
        x = input('Digite o valor do dividendo: ')
        while type(x) != int:
            x = try_int(x)
        y = input('Digite o valor do divisor: ')
        while type(y) != int:
            y = try_int(y)
        calculo_resto(x, y)
    if escolha == '3':
        x = input('Digite o primeiro valor: ')
        while type(x) != int:
            x = try_int(x)
        y = input('Digite o segundo valor: ')
        while type(y) != int:
            y = try_int(y)
        calculo_maximo(x, y)
    if escolha == '4':
        x = input('Digite o número cujo valor absoluto deseja verificar: ')
        while type(x) != int:
            x = try_int(x)
        calculo_absoluto(x)
    if escolha == '5':
        x = input('Digite o valor do número base: ')
        while type(x) != int:
            x = try_int(x)
        y = input('Digite o valor do expoente: ')
        while type(y) != int:
            y = try_int(y) 
        calculo_exponencial(x, y)
    if escolha == 'ESC':
        break
