# Fazer um programa para ler idades e ao final mostrar a media aritmetica das idades.FLAG sera IDADE = -1

continuar = True
soma_idades = 0
numeros_totais = 0

while continuar == True:
    idade = input('Digite uma idade, ou -1 para sair: ')
    try:
        idade = int(idade)               
    except:
        print('Idade inválida.')
        continue
    if idade == -1:
        continuar = False
        break
    if idade < -1:
        print('Idade inválida.')
        continue

    soma_idades += idade
    numeros_totais += 1

print(f'A média aritmética das idades é: {soma_idades/numeros_totais}')
    



