'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e ímpares digitados, respectivamente. Ao final, mostre o conteúdos das 3 listas
geradas.'''

lista = []
lista_par = []
lista_impar = []

while True:
    continuar = ' '
    lista.append(int(input('Informe um número: ')))
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
for p in lista:
    if p % 2 == 0:
        lista_par.append(p)
    else:
        lista_impar.append(p)
print('LISTA COMPLETA', lista)
print('LISTA PAR: ', lista_par)
print('LISTA ÍMPAR: ', lista_impar)
