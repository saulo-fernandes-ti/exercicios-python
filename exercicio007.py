#Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno,
#calcule e mostre a sua média.

n1 = float(input("Digite sua primeira nota:"))
n2 = float(input("Digite sua segunda nota:"))

m = (n1+n2)/2


print('Sua primeira nota é: {}, a segunda é {}, então sua média será {}'.format(n1,n2,m))
