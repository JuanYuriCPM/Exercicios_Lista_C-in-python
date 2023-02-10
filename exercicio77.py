"""
Faça um programa que leia as seguintes informações de um aluno: matrícula, valor da mensalidade, quantidade de meses em atraso e percentual de aumento devido ao atraso.
Este algoritmo deverá calcular e imprimir a matrícula do aluno, o valor da mensalidade, o valor a ser pago com o percentual de aumento mensal e o valor a ser pago
com o percentual de aumento em todos os meses de atraso.
"""

alunos = {

    {
    'Matrícula': '25082022',
    'Mensalidade': 149.99,
    'Meses em atraso': 2,
    'Percentual de aumento por atraso': 5,
    },
    
    {
    'Matrícula': '79862022',
    'Mensalidade': 149.99,
    'Meses em atraso': 2,
    'Percentual de aumento por atraso': 5,
    }
}
verificacao = None
periodo_de_atraso = None
valor_total_devido = 0

while True:
    matricula = input('Digite a matrícula que deseja verificar: ')
    verificacao = None
    while not verificacao:
        try:
            if len(matricula) != 8 or int(matricula) < 0:
                print(alunos.values())
                matricula = input('Matrícula inválida, digite um número de 8 digitos: ')
                continue 
            for i in alunos:
                    if matricula == alunos[i]['Matrícula']:
                        for j in alunos[i]:
                            print(f'{j}: {alunos[i][j]}')
                        print('O valor individual das mensalidades atrasadas é de:')
                        periodo_de_atraso = alunos[i]['Meses em atraso']
                        mensalidade = alunos[i]['Mensalidade']
                        percentual_de_atraso = alunos[i]['Percentual de aumento por atraso']
                        while periodo_de_atraso > 0:
                            valor_parcela_atrasada = mensalidade * ((1+(percentual_de_atraso/100))**periodo_de_atraso)
                            print(f'Mês Atrasado {periodo_de_atraso}: {round(valor_parcela_atrasada, 2)}R$')
                            valor_total_devido += valor_parcela_atrasada
                            periodo_de_atraso -= 1
                        print(f'O valor total devido é de: {round(valor_total_devido, 2)}R$')
                        verificacao = True
                        valor_total_devido = 0
        except:
            matricula = input('Matrícula inválida, digite um número de 8 digitos: ')
