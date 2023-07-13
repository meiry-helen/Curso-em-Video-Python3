#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro nome e o último nome separadamente.
#Ex: "Ana Maria de Souza" / primeiro = Ana / último = Souza

nome = input('Informe seu nome: ').strip()
nome_dividido = nome.split()

print('Primeiro nome: ', nome_dividido[0])
print('Último nome: ', nome_dividido[len(nome_dividido)-1])

