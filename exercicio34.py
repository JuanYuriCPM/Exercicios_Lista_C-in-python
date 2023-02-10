# 34 - Faca um programa que leia a idade de uma pessoa e informe a sua classe eleitoral: nao eleitor (abaixo de 16 anos), eleitor obrigatorio (entre 18 e 65 anos), ou eleitor facultativo (entre 16 e 18 anos e acima de 65 anos)

idade = input('Digite a sua idade: ')

idade = int(idade)

if idade < 16:
    print('Sua classe eleitoral é: Não Eleitor')
elif idade >= 18 and idade <= 65:
    print('Sua classe eleitoral é: Eleitor Obrigatório')
else:
    print('Sua classe eleitoral é: Eleitor Facultativo')