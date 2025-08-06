#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Valor do dólar US$ visto em 05/08/2025

d = float(input('Digite o R$ que tem na carteira: '))
c = d/5.50
print('Saldo atual:{} em R$'.format(d))
print('Saldo em dólar:{:.2} em  US$'.format(c))

