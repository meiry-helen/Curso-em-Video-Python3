'''Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra
quando ele disser que quer mostrar 0 termos'''

t_inicial = int(input('Informe o termo inicial: '))
razão = int(input("Informe a razão da PA: "))
n_termos = 9
i = 0
j = t_inicial
while i != n_termos + 1:
    print(j, end=' ')
    j += razão
    if i == n_termos:
        n_termos = int(input('\n\nDigite 0 para finalizar.\nOu deseja adicionar mais termos: '))
        i = 0
    i += 1
    if n_termos == 0:
        break
