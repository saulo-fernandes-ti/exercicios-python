#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Digite seu salário atual:'))
sn = s + (s*15/100)

print('Seu salário com 15% de aumento:{} R$'.format(sn))
