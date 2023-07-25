'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
lista = []
n = 0
#aux = 0
for i in range(0, 5):
    n = int(input('Informe um número: '))
    if i == 0 or n > lista[- 1]:        #lista[len(lista) - 1]
        lista.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(f'Os valores digitados foram: {lista}')


'''aux = n
print('Adicionado ao final da lista.')
else:
for i, v in enumerate(lista):
    n = int(input('Informe um número: '))
    if n > aux:
        lista.append(n)
        print('Número adicionado na posição', lista.index(n))
    elif n == aux:
    else:
        lista.insert()'''
