#Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu

import random
from time import sleep

num = random.randint(0,  5)

tentativa = int(input('Em que número estou pensando? '))
print('PROCESSANDO...')
sleep(2)
if num == tentativa:
    print('Você adivinhou! Você venceu!')
else:
    print('Você perdeu! O número era {}'.format(num))