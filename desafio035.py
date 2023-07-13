#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
# não formar um triângulo.

segmento1 = float(input('Informe o comprimento da reta 1: '))
segmento2 = float(input('Informe o comprimento da reta 2: '))
segmento3 = float(input('Informe o comprimento da reta 3: '))

if segmento1 + segmento2 > segmento3 and segmento1 + segmento3 > segmento2 and segmento2 + segmento3 > segmento1:
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo')
