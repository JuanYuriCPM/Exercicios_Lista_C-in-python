# 13 - Faça um programa para efetuar o cálculo de uma prestação em atraso utilizando a seguinte fórmula:
# valor + (valor * (taxa/100) * tempo), onde os dados valor(real), taxa(real) e tempo(int) devem ser lidos

valor = input('Digite o valor inicial da prestação em atraso:')
taxa = input('Digite o valor da taxa de atraso:')
tempo = input('Digite o tempo total de atraso (em meses):')

valor = int(valor)
taxa = int(taxa)
tempo = int(tempo)
valor_final = valor + (valor * (taxa/100) * tempo)

print('O valor final da prestação em atraso é de:', valor_final)