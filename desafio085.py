'''Crie um programa onde os usuários possam digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

numeros = [[],[]]

for c in range(0, 7):
    n = (int(input('Informe um número: ')))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
#sorted(numeros[0])
#sorted(numeros[1])
print(f'Números pares digitados: {sorted(numeros[0])}')
print(f'Números ímpares digitados: {sorted(numeros[1])}')