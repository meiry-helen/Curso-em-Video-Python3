#Escreva um programa que leia dos números inteiros e compare-os mostrando na tela uma mensagem:
#O primeiro valor é maior; o segundo valor é maior ou não existe valor maios - os dois são iguais.

n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))

if n1 > n2:
    print('O primeiro número é maior.')
elif n2 > n1:
    print('O segundo número é maior.')
else:
    print('Os números são iguais.')
