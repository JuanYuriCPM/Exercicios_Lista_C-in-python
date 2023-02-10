# 57 - Fazer um programa para ler notas e ao final mostrar o percentual de alunos aprovados (nota > 60).Flag sera Nota = -1

continuar = True
alunos = 0
aprovados = 0

while continuar is True:
    nota = input('Digite uma nota (ou digite "-1" para sair): ')
    try:
        nota = int(nota)
        if nota < -1 or nota > 100:
            print('Nota inválida.Por favor digite um valor entre 0 e 100.')
            continue
        elif nota == -1:
            break
    except:
        print('Nota inválida.Por favor digite um valor entre 0 e 100.')
        continue
    alunos += 1
    if nota > 60:
        aprovados += 1

print(f'O percentual de alunos aprovados é de: {100*aprovados/alunos}%')
    


