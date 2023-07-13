#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input("Informe seu nome: ").upper().strip()
res = 'SILVA' in nome
if res == True:
    print('Seu nome tem SILVA')
else:
    print('Seu nome não tem SILVA')
