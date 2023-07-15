n = int(input('Informe um número: '))
soma = 1
resultado_final = 0
valor = 1
while soma < n:
    valor += 2
    soma += valor
if soma > n:
    print('PERAI... TÁ LIDANDO ERRADO!')
else:
    print(valor)
