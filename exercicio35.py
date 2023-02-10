""" 
35 - Entrar com o salario de uma pessoa e imprimir o desconto do INSS segundo a tabela abaixo:

- menor ou igual a 600,00: isento
- maior que 600,00 e menor ou igual a 1.200,00: 20%
- maior que 1.200,00 e menor ou igual a 2.000,00: 25%
- maior que 2.000,00: 30% */
"""

salario = input('Digite o salário a ser analisado: ')

salario = float(salario)

if salario <= 600:
    print('Seu desconto do INSS é: Isento')
elif salario > 600 and salario <= 1200:
    print('Seu desconto do INSS é: 20%')
elif salario > 1200 and salario <= 2000:
    print('Seu desconto do INSS é: 25%')
else:
    print('Seu desconto do INSS é: 30%')
