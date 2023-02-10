# 33 - Faca um programa que leia 3 notas de um aluno, calcule a sua media aritmetica e imprima uma mensagem dizendo se o aluno foi aprovado, 
# reprovado ou devera fazer prova final.
#O criterio de aprovacao e o seguinte: aprovado (media >= 7), reprovado (media < 3) ou prova final (3 =< media <= 7)

nome = input('Digite o nome do aluno: ')
nota1 = input('Digite a primeira nota: ')
nota2 = input('Digite a segunda nota: ')
nota3 = input('Digite a terceira nota: ')

nota1 = int(nota1)
nota2 = int(nota2)
nota3 = int(nota3)

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f'{nome}: Aprovado')
elif media <=7 and media >= 3:
    print(f'{nome}: Prova Final')
else:
    print(f'{nome}: Reprovado')