#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo é formado:
#EQUILÁTERO: todos os lados são iguais
#ISÓSCELES: dois lados iguais
#ESCALENO: todos os lados diferentes

seg1 = float(input('Informe o comprimento do segmento 1: '))
seg2 = float(input('Informe o comprimento do segmento 2: '))
seg3 = float(input('Informe o comprimento do segmento 3: '))

if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1:
    print('É um triângulo do tipo:')
    if seg1 == seg2 == seg3:
        print('Equilátero!')
    elif seg1 == seg2 != seg3 or seg1 == seg3 != seg2 or seg3 == seg2 != seg1:
        print('Isósceles!')
    else:
        print('Escaleno')
else:
    print('Não é um triângulo!')