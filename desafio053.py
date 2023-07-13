#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

palindromo = str(input('Digite a frase para saber se é um palindromo: ')).strip().replace(" ", "")
t = len(palindromo)
inverso = ''
for c in range(0, t):
    inverso += (palindromo[(t-1)-c])
#print(inverso)
if palindromo == inverso:
    print('É um palíndromo!')
else:
    print(('Não é um palíndromo!'))
print(palindromo)
print(inverso)
