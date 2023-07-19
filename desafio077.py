'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais.'''

palavras = ('cadeira', 'cha', 'paralelepipedo', 'muqueca', 'professora')

'''letra = ' '
for i in palavras:
    print(palavras[c], end='                ')
    if 'a' in palavras[c]:
        print('a', end=' ')
    if 'e' in palavras[c]:
        print('e', end=' ')
    if 'i' in palavras[c]:
        print('i', end=' ')
    if 'o' in palavras[c]:
        print('o', end=' ')
    if 'u' in palavras[c]:
        print('u', end=' ')
    print('\n')
    c += 1'''
'''l = 0
c = 0
VOGAIS = 'aeiou'
for i in palavras:
    print(f'{palavras[c]}.......', end=' ')
    for letra in VOGAIS:
        if letra in palavras[c]:
            print(letra, end=' ')
        l += 1
    print(sep=' ')
    c += 1'''

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
