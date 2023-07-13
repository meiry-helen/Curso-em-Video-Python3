#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Informe um número: '))
qtd = 0
for c in range(1, n):
    if n % c == 0:
        qtd = qtd + 1

if qtd == 1:
    print('O número é primo!')
else:
    print('O número não é primo!')