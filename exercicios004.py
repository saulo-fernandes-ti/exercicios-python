# Exercício Python 4
# Programa que lê algo pelo teclado e mostra seu tipo primitivo e várias informações

v = input('Digite algo: ')

print('O tipo primitivo do que você digitou é:', type(v))
print('Só tem espaços?', v.isspace())
print('É um número?', v.isnumeric())
print('É alfabético?', v.isalpha())
print('É alfanumérico?', v.isalnum())
print('Está em maiúsculas?', v.isupper())
print('Está em minúsculas?', v.islower())
print('Está capitalizado (título)?', v.istitle())
