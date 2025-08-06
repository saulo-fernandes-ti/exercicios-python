#Exercício Python 8: Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.

n1 = int(input('Digite uma quantidade de metros:'))
c = n1 * 100
m = n1 * 1000

print('{} metros, equivalem a {} centímetros e {} milímetros'
	.format(n1,c,m))
