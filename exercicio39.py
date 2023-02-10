""" 39 - Faca um programa que imprima o menu abaixo e exiba o estado civil informado.Exibir uma ensagem de erro caso seja fornecido uma opcao invalida.

1 - solteiro
2 - separado
3 - casado
4 - divorciado
5 - viuvo 
"""

estado_civil = input('Opções de estado civil: \n\n1 - solteiro\n2 - separado\n3 - casado\n4 - divorciado\n5 - viuvo\n\nDigite sua opção: ')

if estado_civil == '1':
    print('O estado civil informado é: Solteiro')
elif estado_civil == '2':
    print('O estado civil informado é: Separado')
elif estado_civil == '3':
    print('O estado civil informado é: Casado')
elif estado_civil == '4':
    print('O estado civil informado é: Divorciado')
elif estado_civil == '5':
    print('O estado civil informado é: Viúvo')
else:
    print('Erro: Opção inválida')
