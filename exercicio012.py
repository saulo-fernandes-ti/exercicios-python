#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Digite um valor de um produto:'))
desconto = produto - (produto*5/100)

print('Valor sem desconto {} R$ e com desconto {} R$'.format(produto, desconto))
