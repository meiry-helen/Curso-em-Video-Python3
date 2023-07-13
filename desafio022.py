# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1 - O nome com todas as letras maiúsculas
# 2 - O nome com todas as letras minúsculas
# 3 - Quantas letras ao todo sem considerar espaços
# 4 - Quantas letras tem o primeiro nome

nome = str(input('Qual o seu nome? ')).strip()
print(nome.upper())
print(nome.lower())
lista = nome.split()
sem_espacos = ''.join(lista)
print(len(sem_espacos))
print(len(lista[0]))
