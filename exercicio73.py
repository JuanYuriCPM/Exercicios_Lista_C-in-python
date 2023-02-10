def try_int(numero):
    try:
        numero = int(numero)
        return numero
    except:
        numero = input('Input inválido.Por favor digitar um número inteiro: ')
        return numero

def calculo_exponencial(x, y):
    return x**y

while True:
        x = input('Digite o valor do número base: ')
        while type(x) != int:
            x = try_int(x)
        y = input('Digite o valor do expoente: ')
        while type(y) != int:
            y = try_int(y) 
        print(calculo_exponencial(x, y))
        break