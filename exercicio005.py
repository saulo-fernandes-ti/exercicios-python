#Exercício Python 5: Faça um programa que leia um número Inteiro 
#e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número:'))
s = n + 1
a = n - 1

print('Seu número é {}, o seu sucessor é :{}, e seu antecessor é: {}' 
.format(n,s,a))
