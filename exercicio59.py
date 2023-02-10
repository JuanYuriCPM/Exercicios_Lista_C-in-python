# 59 - Fazer um programa para calcular o fatorial de um numero qualquer

numero = input('Digite um número positivo inteiro a ser calculado o valor fatorial: ')

while True:
    try:
        numero = int(numero)
        if numero <= 0:
            print('Número inválido.')
            continue
        else:
            break   
    except:
        print('Número inválido.')
        continue

fatorial = range(0,numero, 1)
total = 1

for valor in fatorial:
    total *= numero
    numero -= 1

print(total)
