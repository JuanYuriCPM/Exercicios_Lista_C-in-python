# Faca um programa que leia um numero de entrada e imprima os numeros de 0 ate o numero lido

while True:
    numero = input('Digite um número: ')
    contador = 0
    
    try:
        numero = int(numero)
    except:
        numero = None
    
    if numero is None:
        print('Número inválido.Favor digitar um número válido.')
        continue

    if contador <= numero: 
        while contador <= numero:
            print(contador)
            contador += 1            
    elif contador >= numero:
        while contador >= numero:
            print(contador)
            contador -= 1
            
    break