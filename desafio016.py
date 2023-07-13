#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex: Digite o número 6.127 - O número 6.127 tem a parte inteira 6.

from math import trunc

n = float(input('Digite um número real: '))
print('A parte inteira do número {} é {}'.format(n, trunc(n)))
