# Exercício Python 4
# Programa que lê algo pelo teclado e mostra seu tipo primitivo e várias informações

v1 = input('Digite algo: ')

print('O tipo primitivo do que você digitou é:', type(v1)
print('Só tem espaços?', v1.isspace())
print('É um número?', v1.isnumeric())
print('É alfabético?', v1.isalpha())
print('É alfanumérico?', v1.isalnum())
print('Está em maiúsculas?', v1.isupper())
print('Está em minúsculas?', v1.islower())
print('Está capitalizado (título)?', v1.istitle())
