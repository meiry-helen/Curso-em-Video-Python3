#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, tan, cos, degrees, radians

angulo = int(input('Informe o ângulo: '))

rad = radians(angulo)
s = sin(rad)
c = cos(rad)
t = tan(rad)


print('seno {:.2f}, cosseno {:.2f}, tangente {:.2f}'.format(s, c, t))
