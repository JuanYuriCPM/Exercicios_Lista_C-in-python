"""
Fazer um programa para ler uma agenda telefonica com a estrutura abaixo e mostra aqueles que fazem 
aniversario no mes fornecido.A agenda contem 100 registros e o lay-out da agenda e o seguinte: nome,
endereco, telefone, aniversario (formato: dd/mm/aaaa).
"""
verificacao = None

lista_telefonica = {
    'Pessoa_1': {
    'nome': 'Juan',
    'endereço': 'Rua Barão de Cotegipe',
    'telefone': '2572-6030',
    'aniversario': ['13', '09', '2003'],
    },

    'Pessoa_2': {
    'nome': 'Karine',
    'endereço': 'Rua das Gordinhas',
    'telefone': '2786-3040',
    'aniversario': ['25', '08', '1910'],
    },

    'Pessoa_3': {
    'nome': 'Alan',
    'endereço': 'Rua dos Obesos',
    'telefone': '3090-3021',
    'aniversario': ['14', '03', '1923'],
    },
}

mes = input('Digite qual mês deseja verificar (número de 2 digitos): ')
while not verificacao:
    try:
        if len(mes) != 2 or int(mes) <= 0 or int(mes) > 12:
            mes = input('Mês inválido, digite um número de 2 digitos: ')
            continue
        verificacao = True
    except:
        mes = input('Mês inválido, digite um número de 2 digitos: ')

for i in lista_telefonica:
    if lista_telefonica[i]['aniversario'][1] == mes:
        for j in lista_telefonica[i]:
                print(f'{j}: {lista_telefonica[i][j]}')