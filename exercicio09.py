# 9 - Faça um programa que leia dois números e imprima a seguinte saída:
# Dividendo, Divisor, Quociente e resto, sendo cada um em uma linha.

dividendo = input('Digite o dividendo: ')
divisor = input('Digite o divisor: ')

dividendo = int(dividendo)
divisor = int(divisor)
quociente = dividendo / divisor
resto = dividendo % divisor

print('Dividendo:', dividendo)
print('Divisor:', divisor)
print('Quociente:', quociente)
print('Resto:', resto)
