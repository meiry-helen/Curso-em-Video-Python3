#Faça um programa que leia uma frase pelo teclado e mostre>
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece na última vez.

frase = input('Digite uma frase: ').upper().strip()
print('A quantidade de letras As: ', frase.count('A'))
print('A primeira letra A aparece no índice: ', frase.find('A'))
print('A última letra A aparece no índice: ', frase.rfind('A'))
