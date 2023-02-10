"""
Fazer um programa para ler 100 registros, cujos dados estao descritos abaixo, e 
forneca o percentual de mulheres com idade entre 18 e 35, de olhos verdes e cabelos 
louros. Registro: sexo(m,f), olhos(azuis, verdes, pretos), cabelo(louro, castanho, 
preto) e idade(int) 
"""

registro = {
    'sexo': None,
    'olhos': None,
    'cabelo': None,
    'idade': None,
}

sexos = ['m', 'f']
cores_cabelo = ['louro', 'castanho', 'preto']
cores_olhos = ['azuis', 'verdes', 'pretos']
qualificadas = 0
candidatos_totais = 0


total_registros = 100

while total_registros > 0:
        sexo = input('Digite o sexo (M) ou (F): ')
        sexo = sexo.lower()
        while sexo not in sexos:
            sexo = input('Sexo inválido, por favor digite (M) ou (F)') 
        
        olhos = input('Digite a cor do olhos (azuis, verdes ou pretos): ')
        olhos = olhos.lower()
        while olhos not in cores_olhos:
            olhos = input('Cor de olhos inválida, por favor digite uma cor válida (azuis, verdes ou pretos): ')
        
        cabelo = input('Digite a cor do cabelo (louro, castanho, preto): ')
        cabelo = cabelo.lower()
        while cabelo not in cores_cabelo:
            cabelo = input('Cor de cabelo inválida, por favor digite uma opção válida (louro, castanho, preto): ')
        
        idade = input('Digite a idade: ')
        while type(idade) == str or int(idade) <= 0:
            try:
                idade = int(idade)
                if idade <= 0:
                    idade = input('Idade inválida.Por favor digite um número inteiro maior que 0: ')
            except:
                idade = input('Idade inválida.Por favor digite um número inteiro maior que 0: ')

        registro_atualizado = [['sexo', sexo], ['olhos', olhos], ['cabelo', cabelo], ['idade', idade]]
        registro.update(registro_atualizado)
        total_registros -= 1
        candidatos_totais += 1
        if idade > 18 and idade < 35:
            if sexo == 'f':
                if cabelo == 'louro':
                    if olhos == 'verdes':
                        qualificadas += 1
        print(registro)

print(f'O percentual de mulheres com idade entre 18 e 35, de olhos verdes e cabelos louros é de: {(qualificadas * 100)/candidatos_totais}%')

