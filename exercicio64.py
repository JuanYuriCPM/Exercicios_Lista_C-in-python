"""
Faca um programa que leia uma temperatura em Celsisus e chame uma funcao que a exiba em Fahrenheit

sendo que fahrenheit = (1.8f*celsius) + 32
"""

def conversao_fahrenheit(celsius):
    fahrenheit= (1.8*celsius) + 32
    print(f'\nA temperatura em celsius digitada, convertida para fahrenheit é igual a: {fahrenheit}° fahrenheit\n ')

while True:
    celsius = input('Digite a temperatura em celsius: ')
    try:
        celsius = float(celsius)
    except:
        print("\nInput inválido.Por favor digite apenas números válidos.\n")
        continue
    
    conversao_fahrenheit(celsius)
    




