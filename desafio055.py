#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
peso_maior = 0
peso_menor = 0
for c in range(0, 5):
    peso = float(input('Informe o peso: '))
    if c == 0:
        peso_maior = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        elif peso < peso_menor:
            peso_menor = peso

print('O maior peso informado foi {:.1f}'.format(peso_maior))
print('O menor peso informado foi {:.1f}'.format(peso_menor))
