#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km
#percorridos por um carro alugado e a quantidade de dias pelos quais ele
#foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite a quantidade de km percorridos pelo carro:'))
d = int(input('Digite a quantidade de dias que alugou o carro:'))

pg = (d * 60) + (km * 0.15)

print('O total a pagar é R$ {:.2f}'.format(pg))
