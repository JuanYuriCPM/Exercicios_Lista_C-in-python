# 37 - Entrar com nome, idade e sexo (M, m, F, f) de uma pessoa.Se a pessoa for do sexo feminino e tiver menos de 25 anos, 
# entao imprimir nome e mensagem "ACEITA", caso contrario imprima nome e mensagem "NAO ACEITA"

nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')
sexo = input('Digite o seu sexo (M) ou (F): ')

idade = int(idade)

if idade < 25 and (sexo == 'F' or sexo == 'f'):
    print(f'{nome}: ACEITA')
else:
    print(f'{nome}: NÃO ACEITA')