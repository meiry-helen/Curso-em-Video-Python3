'''Melhore o jogo do desafio028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer'''

import random
from time import sleep

palpite_cpu = random.randint(0, 10)
n = -1
c = 0
while n != palpite_cpu:
    n = int(input('Faça seu palpite: '))
    c += 1
    sleep(0.5)
print('Você acertou!\nVocê fez {} tentativa(s)'.format(c))
