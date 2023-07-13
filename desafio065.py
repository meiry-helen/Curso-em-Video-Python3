'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores.'''

n = media = soma = qtd_n = 0
maior = menor = 0
resp = ''
while resp != 'n':
    n = int(input('Informe um valor: '))
    soma += n
    qtd_n += 1
    if qtd_n == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja continuar (n/s): ')).lower().strip()[0]
media = soma / qtd_n
print('Maior valor é {} e menor valor é {}'.format(maior, menor))
print('A média dos números informados é {}'.format(media))
