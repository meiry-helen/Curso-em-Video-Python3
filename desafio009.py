n = int(input('Informe um número para saber sua tabuada: '))
# i = -1
print('-' * 12)
for i in range(11):
    print('{} x {:2} = {}'.format(n, i, i * n))
print('-' * 12)
