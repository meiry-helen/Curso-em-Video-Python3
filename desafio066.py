'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
999, que é a condição de parada. No final, mostre quantos números foram digitados e qual a soma entre eles, desconsiderando
a flag.'''

soma = i = 0
while True:
    n = int(input('Informe um número [digite 999 para parar]: '))
    if n == 999:
        break
    i += 1
    soma += n
print(f'Foram informados {i} números e a soma deles é igual a {soma}')
