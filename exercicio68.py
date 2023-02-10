"""
Faca um programa que leia tres caracteres e os passe a uma funcao que ira ordena-los e exibi-los em
ordem crescente

"""

def ordem_crescente(a, b, c):
    if a >= b and b >= c:
        print(f'\nA ordem crescente é: {c}, {b}, `{a}\n')
    elif a >= c and c >= b:
        print(f'\nA ordem crescente é: {b}, {c}, {a}\n')
    elif b >= a and a >= c:
        print(f'\nA ordem crescente é: {c}, {a}, {b}\n')
    elif b >= c and c >= a:
        print(f'\nA ordem crescente é: {a}, {c}, {b}\n')
    elif c >= a and a >= b:
        print(f'\nA ordem crescente é: {b}, {a}, {c}\n')
    else:
        print(f'\nA ordem crescente é: {a}, {b}, {c}\n')

while True:
    a = input('Digite o primeiro valor a ser comparado (valor a): ')
    try:
        a = float(a)
    except:
            print('\nInput inválido.\n')
            continue
    b = input('Digite o segundo valor a ser comparado (valor b): ')
    try:
        b = float(b)
    except:
            print('\nInput inválido.\n')
            continue
    c = input('Digite o terceiro valor a ser comparado (valor c): ')
    try:
        c = float(c)
    except:
            print('\nInput inválido.\n')
            continue
    
    ordem_crescente(a, b, c)