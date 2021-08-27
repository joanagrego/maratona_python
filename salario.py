'''URI Online Judge | 1008
Salário

Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas,
 o valor que recebe por hora e calcula o salário desse funcionário.
 A seguir, mostre o número e o salário do funcionário, com duas casas decimais.'''

num = int(input())
qnt = int(input())
salario = float(input())

print(f'NUMBER = {num}')
print(f'SALARY = U$ {qnt*salario:.2f}')