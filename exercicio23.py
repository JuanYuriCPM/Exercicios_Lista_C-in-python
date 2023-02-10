# 23 - Faca um programa para ler nome e nota de um aluno e informar o nome do aluno seguido de sua situacao: Aprovado (nota > 7), Reprovado (nota < 5), ou prova final (nota>= 5 e <=7)

nome = input('Digite o nome do aluno: ')
nota = input('Digite a nota do aluno: ')

nota = int(nota)

if nota > 7:
    print(f'{nome}: Aprovado')
elif nota <= 7 and nota >= 5:
    print(f'{nome}: Prova Final')
else:
    print(f'{nome}: Reprovado')