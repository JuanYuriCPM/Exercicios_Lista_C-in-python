# 14 - Faça um programa que apresente a conversão em dólar para real sendo passados os valores reais e a taxa de conversão

dolar = input('Digite o valor em dólar a ser convertido:')
taxa = input('Digite o valor da taxa de conversão: ')

dolar = float(dolar)
taxa = float(taxa)
real = dolar * taxa

print('O valor em reais da quantidade convertida é de:', real)