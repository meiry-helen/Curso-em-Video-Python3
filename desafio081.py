'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados;
B) A lista ordenada de forma decrescente;
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
while True:
    continuar = ' '
    lista.append(int(input('Informe um número: ')))
    while continuar != 'N' and continuar != 'S':
        continuar = str(input('Número adicionado com sucesso. Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Foram digitados {len(lista)} números')
if 5 in lista:
    print('O número 5 se encontra na lista. ')
else:
    print('O número 5 não está na lista.')
lista.sort(reverse=True)
print(lista)

'''lista_ordenada = sorted(lista)
print('Lista em ordem decrescente: ', end=' ')
for i in reversed(lista_ordenada):
    print(i, end=' ')'''
