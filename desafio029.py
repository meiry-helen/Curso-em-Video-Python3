#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostr
# e a mensagem dizendo que ele foi multado.
#A multa vai custar 7 reais por cada Km excedente.

velocidade = int(input('Qual a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Você foi multado! Multa de R$ {:.2f}".format(multa))
else:
    print('Velocidade permitida!')
