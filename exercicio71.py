""" Faca um programa que leia notas e ao final imprima os seguintes dados usando funcoes: 

- A maior e a menor nota
- A media das notas
- O produto das notas
- O percentual de alunos aprovados (notas > 6) */ """

maior_nota = None
menor_nota = None
total_notas = 0
alunos = 0
aprovados = 0
produto_notas = 1
escolhas = ['1', '2', '3', '4']

def calculo_maior_menor_notas(maior_nota, menor_nota):
    print(f'\nA menor nota e a maior nota são, respectivamente: {menor_nota} e {maior_nota}')
def calculo_media_notas(total_notas, alunos):
        media_notas = total_notas/alunos
        print(f'A média das notas é: {media_notas}')
def calculo_produto_notas(produto_notas):
        print(f'O produto das notas é: {produto_notas}')
def calculo_percentual_aprovados(aprovados, alunos):
        percentual_aprovados = (aprovados*100)/alunos
        print(f'O percentual de alunos aprovados é: {percentual_aprovados}%\n')
def try_float(nota):
    try:
        nota = float(nota)
        if nota < 0 or nota > 10:
            nota = input('\nNota inválida.Por favor digite uma nota contendo apenas números entre 0 e 10: ')
            return nota
        return nota
    except:
        nota = input('\nNota inválida.Por favor digite uma nota contendo apenas números entre 0 e 10: ')
        return nota

        
while True:
    escolha = input("\nMenu:\n\n1 - Adicionar uma nota\n2 - Exibir dados calculados\n3 - Resetar valores\n4 - Sair\n\nDigite uma opção: ")
    while escolha not in escolhas:
            escolha = input('Escolha inválida.Por favor escolha uma opção: ')
    if escolha == '1':
        nota = input('\nDigite uma nota a ser adicionada: ')
        while type(nota) != float or nota < 0 or nota > 10:
            nota = try_float(nota)
        if maior_nota == None:
            maior_nota = nota
        if menor_nota == None:
            menor_nota = nota
        if nota > maior_nota:
            maior_nota = nota
        if nota < menor_nota:
            menor_nota = nota
        if nota > 6:
            aprovados += 1
        total_notas += nota
        produto_notas *= nota
        alunos += 1
        print('Nota adicionada.')
        continue
    elif escolha == '2':
        if alunos != 0:
            calculo_maior_menor_notas(maior_nota, menor_nota)
            calculo_media_notas(total_notas, alunos)
            calculo_produto_notas(produto_notas)
            calculo_percentual_aprovados(aprovados, alunos)
        if alunos == 0:
            print('Nenhuma nota foi adicionada.')
    elif escolha == '3':
        alunos = 0
        total_notas = 0
        produto_notas = 1
        maior_nota = 0
        menor_nota = 0
        aprovados = 0
        print('Valores resetados.')
    else:
        break
        


        
