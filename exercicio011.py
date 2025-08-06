#Exercício Python 11: Faça um programa que leia a largura e a altura de uma
#parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, 
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input('Digite a largura de sua parede:'))
a = float(input('Digite a altura da sua parede:'))
ar = l*a
c = ar / 2
print('Sua área para pintura é: {}'.format(ar),'Metros')
print('Com {} litros de tinta vc pinta a área total de sua parede {}cm2'.	format(c,ar))
