'''Faça um programa que leia um número qualquer e mostre seu fatorial.

Ex: 5! = 5x4x3x2x1 = 120'''

fatorial = int(input('Informe o valor que deseja saber o fatorial: '))
i = fatorial
j = 1
print('{}! = '.format(fatorial), end='')
while i > 0:
    print('{}'.format(i), end='')
    print(' x ' if i > 1 else '  = ', end='')
    j *= i
    i -= 1
print('{}'.format(j))
