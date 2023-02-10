# 15 - Faça um programa que calcule e apresente o volume de uma caixa retangular por meio da fórmula:
# volume = comprimento * largura * altura

comprimento = input('Digite o valor do comprimento da caixa:')
largura = input('Digite o valor da largura da caixa:')
altura = input('Digite o valor da altura da caixa:')

comprimento = int(comprimento)
largura = int(largura)
altura = int(altura)
volume = comprimento * largura * altura

print('O valor do volume da caixa é:', volume)