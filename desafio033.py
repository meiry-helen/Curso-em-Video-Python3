# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

if n1 > n2 > n3:
    print('Maior:', n1, '\n''Menor:', n3)
else:
    if n1 > n3 > n2:
        print('Maior:', n1, '\nMenor:', n2)
    else:
        if n2 > n1 > n3:
            print('Maior:', n2, '\nMenor:', n3)
        else:
            if n2 > n3 > n1:
                print('Maior:', n2, '\nMenor:', n1)
            else:
                if n3 > n1 > n2:
                    print('Maior:', n3, '\nMenor:', n2)
                else:
                    print('Maior:', n3, '\nMenor:', n1)
