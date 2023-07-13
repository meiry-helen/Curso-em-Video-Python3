'''Faça um programa que jogue par ou ímpar com o computador. O jogo será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

import random
qtd_vitorias = 0

while True:
    cpu_n = random.randint(0, 10)
    jogador_n = int(input('\nInforme um número: '))
    resultado = cpu_n + jogador_n
    jogada = str(input("Informe a jogada - PAR ou IMPAR: ")).strip().upper()[0]

    if resultado % 2 == 0 and jogada == 'P':
        print(f'Você venceu! O resultado foi {resultado} e você escolheu PAR')   #vitória
        qtd_vitorias += 1
    elif resultado % 2 == 0 and jogada in 'IÍ':
        print(f'Você perdeu! O resultado foi {resultado} e você escolheu ÍMPAR')  #derrota
        break
    elif resultado % 2 != 0 and jogada == 'P':
        print(f'Você perdeu! O resultado foi {resultado} e você escolheu PAR')    #derrota
        break
    else:
        print(f'Você venceu! O resultado foi {resultado} e você escolheu ÍMPAR')   #vitória
        qtd_vitorias += 1
print(f'Você conquistou {qtd_vitorias} vitória(s)!')