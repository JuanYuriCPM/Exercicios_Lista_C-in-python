# 37 - Entrar com o ano de nascimento de uma pessoa e informar a sua idade.Verifique se o ano fornecido e um ano valido. OBS: Exercicio feito em 2022

ano_nascimento = input('Digite o seu ano de nascimento: ')

ano_nascimento = int(ano_nascimento)
idade = 2022 - ano_nascimento

if ano_nascimento >= 1900 and ano_nascimento <= 2022:
    print(f'Sua idade é: {idade} anos')
else:
    print('A data de nascimento inserida não é válida')