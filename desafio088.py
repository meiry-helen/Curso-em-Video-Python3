'''Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint, sample

n_jogos = int(input('Indique o número de jogos: '))
tamanho = 6
valores = range(0, 61)

sorteio = []

for i in range(n_jogos):
    sorteio.append(sample(valores, tamanho))

for i in range(n_jogos):
    for c in range(tamanho):
        print(sorteio[i][c], end=' ')
    print()

