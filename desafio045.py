#Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep

jogador = int(input('[0] - Pedra\n[1] - Papel\n[2] - Tesoura\nEscolha: '))
jogada = ('Pedra', 'Papel', 'Tesoura')
cpu = random.randint(0, 2)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('COMPUTADOR:', jogada[cpu], '\nVOCÊ:', jogada[jogador])
#pedra vence
if jogador == 0 and cpu == 2:
    print('Você venceu!')
elif jogador == 2 and cpu == 0:
    print('Você perdeu!')
#papel vence
elif jogador == 1 and cpu == 0:
    print('Você venceu!')
elif jogador == 0 and cpu == 1:
    print('Você perdeu!')
#tesoura vence
elif jogador == 2 and cpu == 1:
    print('Você venceu!')
elif jogador == 1 and cpu == 2:
    print('Você perdeu!')
#empates
elif jogador == 0 and cpu == 0:
    print('Deu empate!')
elif jogador == 1 and cpu == 1:
    print('Deu empate!')
elif jogador == 2 and cpu == 2:
    print('Deu empate!')
