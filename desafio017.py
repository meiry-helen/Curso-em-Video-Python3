#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
#e mostre o comprimento da hipotenusa.

from math import hypot

x = int(input('Informe o comprimento do cateto oposto: '))
y = int(input('Informe o comprimento do cateto adjacente: '))
print('O comprimento da hipotenusa é {:.2f}'.format(hypot(x, y)))
