#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Informe o número da tabuada que deseja consultar: '))

for c in range(0, 11):
    print('{} x {:2} = {:2}'.format(n, c, n*c))
