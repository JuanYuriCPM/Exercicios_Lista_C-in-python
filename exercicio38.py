"""
38 - Um plano de saude, apos negociacao com o governo, enviou a tabela abaixo.Entrar com nome e idade de uma pessoa e imprimir o nome e o valor que ela devera pagar.

- Ate 10 anos - 30,00
- Maior que 10 e ate 29 - 60,00
- Maior que 29 e ate 45 - 120,00
- Maior que 45 e ate 59 - 150,00
- Maior que 59 e ate 65 - 250,00
- Maior que 65 anos     - 400,00

"""

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

idade = int(idade)

if idade <= 10:
    print(f'{nome}: 30,00')
elif idade > 10 and idade <= 29:
    print(f'{nome}: 60,00')
elif idade > 29 and idade <= 45:
    print(f'{nome}: 120,00')
elif idade > 45 and idade <= 59:
    print(f'{nome}: 150,00')
elif idade > 59 and idade <= 65:
    print(f'{nome}: 250,00')
else:
    print(f'{nome}: 400,00')