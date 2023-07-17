'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) quantas vezes apareceu o valor 9.
B) em que posição foi digitado o primeiro valor 3.
C) quais foram os números pares.'''

numeros = []
n_pares = []
for c in range(0, 4):
    n = int(input('Informe um número: '))
    numeros.append(n)
    if n % 2 == 0:
        n_pares.append(n)
tupla_numeros = tuple(numeros)
print('Você digitou os números:', tupla_numeros)
print('O número 9 apareceu:', tupla_numeros.count(9),'vezes')
if 3 not in tupla_numeros:
    posicao_3 = print('O número 3 não foi digitado.')
else:
    posicao_3 = print('O número 3 aparece pela primeira vez na {}ª posição.'.format(tupla_numeros.index(3) + 1))
print(f'Os números pares são: {n_pares}', end=' ')
