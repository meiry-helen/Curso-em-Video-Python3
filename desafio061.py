'''Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while'''

termo_inicial = int(input('Informe o termo inicial: '))
razão = int(input("Informe a razão da PA: "))
i = 0
j = termo_inicial
while i < 10:
    print(j, end=' - ')
    j += razão
    i += 1
print("FIM")
