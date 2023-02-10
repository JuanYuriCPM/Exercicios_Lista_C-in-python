"""58 - Existem 3 candidatos a uma vaga no senado.Feito a eleicao, os votos sao registrados do seguinte modo:

1 - Voto para candidato 1;
2 - Voto para candidato 2;
3 - Voto para candidato 3;
4 - Voto branco;
5 - Voto nulo;

Deseja-se saber:

- O numero do candidato vencedor;
- O numero de votos em branco;
- O numero de votos nulos;
- O numero de eleitores;

OBS: Nao sao possiveis empates."""

candidato1 = 0
candidato2 = 0
candidato3 = 0
branco = 0
nulo = 0
eleitores = 0
continuar = True

while continuar is True:
    voto = input('Opções de voto: \n\n1 - Voto para Candidato 1\n2 - Voto para Candidato 2\n3 - Voto para Candidato 3\n4 - Voto em Branco\n5 - Voto Nulo\n\nDigite a opção desejada, ou digite "s" para encerrar a votação: ')
    if voto == 's':
        if candidato1 != candidato2 != candidato3:
            break
        else:
            print('\nHá um empate atualmente entre dois ou mais candidatos, por favor continue a votação até um desempate para que seja possível encerrar.\n')
            continue
    try:
        voto = int(voto)
        if voto <= 0 or voto > 5:
            print('\nVoto inválido.\n')
            continue
    except:
        print('\nVoto inválido\n')
        continue
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    elif voto == 4:
        branco += 1
    elif voto == 5:
        nulo += 1

    eleitores += 1
    print('\nVoto efetuado com sucesso!\n')

if candidato1 > candidato2 and candidato1 > candidato3:
    print('O candidato vencedor é: Candidato 1')
elif candidato2 > candidato1 and candidato2 > candidato3:
    print('O candidato vencedor é: Candidato 2')
elif candidato3 > candidato1 and candidato3 > candidato2:
    print('O candidato vencedor é: Candidato 3')

print(f'O número de votos em branco é: {branco}')
print(f'O numero de votos nulos é: {nulo}')
print(f'O número total de eleitores é de: {eleitores}')


    



