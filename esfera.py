'''URI Online Judge | 1011
Esfera

Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R).'''

r = float(input())
pi = 3.14159
vol = (4.0/3)*pi*(r**3)

print(f'VOLUME = {vol:.3f}')