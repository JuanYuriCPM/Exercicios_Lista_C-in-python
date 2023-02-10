# 56 - Fazer um programa para ler idade e ao final mostrar as duas maiores idades.Flag sera IDADE = "-1"

continuar = True
maior_idade = None
segunda_maior_idade = 0
contador = 0

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
        print('Idade inválida.Por favor digite uma idade maior ou igual a 0.')
        continue
    if maior_idade == None:
        maior_idade = idade
        contador += 1
        continue
    if idade > maior_idade:
        segunda_maior_idade = maior_idade
        maior_idade = idade
        contador += 1
    elif idade > segunda_maior_idade and idade <= maior_idade:
        segunda_maior_idade = idade
        contador += 1
    

if contador == 1:
    print(f'Apenas uma idade foi digitada: {maior_idade}')
else:
    print(f'As duas maiores idades são, respectivamente: {segunda_maior_idade} e {maior_idade}')
    