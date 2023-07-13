'''Crie um programa que leia vários números inteiros pelo teclado. O programa só irá parar quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
(desconsiderando o flag)'''

soma = 0
qtd_num = 0
n = 0
while n != 999:
    n = int(input('Informe o número: '))
    if n != 999:
        soma += n
        qtd_num += 1
print('A quantidade de números informada foi {} e a soma entre eles foi de {}'.format(qtd_num, soma))