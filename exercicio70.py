"""
Faca um programa usando funcoes, que possua um menu com opcoes de figuras geometricas afim de obter sua area.As areas sao:

- Quadrado = L * L
- Retangulo = B * H
- Triangulo = B * H / 2
- Trapezio = (B Maior + B Menor) * H/2

O menu deve repetir as opcoes ate se digitar ESC. 
"""

opcao = ''

def calculo_area_quadrado(lado):
    area_quadrado = lado * lado
    print(f'A área do quadrado desejado é: {area_quadrado}')

def calculo_area_retangulo(base, altura):
    area_retangulo = base * altura
    print(f'A área do retangulo desejado é: {area_retangulo}')

def calculo_area_triangulo(base, altura):
    area_triangulo = base * (altura/2)
    print(f'A área do triangulo desejado é: {area_triangulo}')

def calculo_area_trapezio(base_maior, base_menor, altura):
    area_trapezio = (base_maior + base_menor) * (altura/2)
    print(f'A área do trapezio desejado é: {area_trapezio}')


while True:
    print('\nMenu de Opções:\n\n1 - Quadrado\n2 - Retângulo\n3 - Triângulo\n4 - Trapézio\nESC - Sair\n')

    opcao = input('Escolha uma opcao: ')
    if opcao == 'ESC':
        break

    try:
        opcao = int(opcao)
    except:
        print('Opção inválida.')
        continue
    
    if opcao == 1:
        lado = input('Digite o lado do quadrado a ser calculado: ')
        try:
            lado = int(lado)
        except:
            print('Número inválido.')
            continue
        calculo_area_quadrado(lado)
    elif opcao == 2:
        base = input('Digite o valor da base do retângulo a ser calculado: ')
        try:
            base = int(base)
        except:
            print('Número inválido.')
            continue
        altura = input('Digite o valor da altura do retângulo a ser calculado: ')
        try:
            altura = int(altura)
        except:
            print('Número inválido.')
            continue
        calculo_area_retangulo(base, altura)
    elif opcao == 3:
        base = input('Digite o valor da base do triângulo a ser calculado: ')
        try:
            base = int(base)
        except:
            print('Número inválido.')
            continue
        altura = input('Digite o valor da altura do triângulo a ser calculado: ')
        try:
            altura = int(altura)
        except:
            print('Número inválido.')
            continue
        calculo_area_triangulo(base, altura)
    elif opcao == 4:
        base_maior = input('Digite o valor da base maior do trapézio a ser calculado: ')
        try:
            base_maior = int(base_maior)
        except:
            print('Número inválido.')
            continue
        base_menor = input('Digite o valor da base menor do trapézio a ser calculado: ')
        try:
            base_menor = int(base_menor)
        except:
            print('Número inválido.')
            continue
        altura = input('Digite o valor da altura do trapézio a ser calculado: ')
        try:
            altura = int(altura)
        except:
            print('Número inválido.')
            continue
        calculo_area_trapezio(base_maior, base_menor, altura)
    else:
        print('Opção inválida.')
        continue