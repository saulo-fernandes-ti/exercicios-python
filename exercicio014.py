#Exercício Python 14: Escreva um programa que converta uma temperatura 
#digitando em graus Celsius e converta para graus Fahrenheit.

#Formúla da conversão °F = (°C × 9/5) + 32

c = float(input('Digite a quantidade de Celsius:°'))
f = (c * 9/5) + 32
print('°{} Celsius corresponde á °{} Fahrenheit  '.
format(c,f))
