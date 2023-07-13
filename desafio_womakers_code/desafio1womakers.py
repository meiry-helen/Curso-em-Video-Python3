def operations(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b
    return soma, subtracao, multiplicacao, divisao


a = float(input('Informe um número: '))
b = float(input('Informe outro número: '))

resultado = operations(a, b)

print('Resultado da soma', resultado[0])
print('Resultado da subtração', resultado[1])
print('Resultado da multiplicação', resultado[2])
print('Resultado da divisão {:.2f}'.format(resultado[3]))
