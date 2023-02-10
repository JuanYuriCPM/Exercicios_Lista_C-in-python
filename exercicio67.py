"""
Faca um programa que receba o preco de uma mercadoria e um percentual de aumento e que chame uma
funcao que receba esses dois parametros e calcule o novo preco da mercadoria com base no percentual
passado.Feit isso entao retorne o novo preco calculado para ser exibido na funcao main.
"""

def calculo_aumento(preco, aumento):
    total = preco + (preco * aumento/100)
    return total

while True:
    preco = input('Digite o preço base para se calcular o aumento: ')
    try:
        preco = float(preco)
    except:
        print('\nPreço inválido.Por favor digite apenas números.\n')
        continue
    
    aumento = input('\nDigite o percentual de aumento: ')
    try:
        aumento = float(aumento)
    except:
        print('\nPercentual de aumento inválido.Por favor digite apenas números.\n')
        continue

    print(f'\nO valor total após o aumento é de:  {calculo_aumento(preco, aumento)}\n')