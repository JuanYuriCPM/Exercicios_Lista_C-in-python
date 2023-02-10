# Fazer um programa para ler numeros inteiros e ao final mostrar o maior e o menor numero digitados.Flag sera NRO = "-1".

continuar = True
maior_numero = 0
menor_numero = None

while continuar == True:
    numero = input('Digite um número inteiro positivo, ou -1 para sair: ')
    try:
        numero = int(numero)               
    except:
        print('Idade inválida.')
        continue
    if numero == -1:
        continuar = False
        break
    if numero < -1:
        print('Idade inválida.')
        continue
    if menor_numero == None:
        menor_numero = numero
    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero

print(f'O menor número e o maior número digitados, respectivamente, são: {menor_numero} e {maior_numero}')
    

