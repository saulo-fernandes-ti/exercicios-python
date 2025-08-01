#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro,
#triplo e raiz quadrada.

n = int(input('Digite um número:'))

d =  n * 2
t =  n * 3
rq = n ** (1/2)

print('Seu número é este:{}'.format(n))
print('Seu dobro é: {}'.format(d))
print('E seu triplo é: {}'.format(t))
print('E sua raiz quadrada é: {}'.format(rq))
