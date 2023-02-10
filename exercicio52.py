# Fazer um programa para ler numeros inteiros e ao final mostrar o maior numero digitado.FLAG sera NRO = -1 

continuar = True
maior_numero = 0

while continuar == True:
    numero = input('Digite um número inteiro positivo, ou -1 para sair: ')
    try:
        numero = int(numero)               
    except:
        print('Número inválido.')
        continue
    if numero == -1:
        continuar = False
        break
    if numero < -1:
        print('Número inválido.')
        continue
    if numero > maior_numero:
        maior_numero = numero

print(f'O maior número digitado é: {maior_numero}')
    


