"""
Crie uma funcao que receba o ano e retorne 1 caso esse ano seja bissexto e 0 se este ano nao for bissexto.
Dica: um ano e bissexto se for divisivel por 400
"""

def calculo_bissexto(ano):
    return ano % 400 == 0

while True:
    ano = input('Digite o ano a ser avaliado: ')
    try:
        ano = int(ano)
    except:
        print('\nInput inválido.Por favor digite apenas números inteiros positivos.\n')
        continue

    print(f'\nO retorno é: {calculo_bissexto(ano)}\n')