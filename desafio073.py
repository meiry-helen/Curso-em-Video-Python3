'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
colocação. Depois, mostre:

A) apenas os 5 primeiros colocados.
B) os últimos 4 colocados da tabela.
C) uma lista com os times em ordem alfabética.
D) em que posição na tabela está o time da Chapecoense.'''

campeonato = ('Botafogo', 'Flamengo', 'Grêmio', 'Fluminense', 'Palmeiras', 'Bragantino', 'Fortaleza', 'São Paulo', 'Cruzeiro', 'Internacional', 'Athletico-PR', 'Athletico-MG', 'Santos', 'Cuiabá', 'Corinthians', 'Bahia', 'Goiás', 'Coritiba', 'Vasco da Gama', 'América-MG')

print('-'*60)
print('{:^60}'.format('5 PRIMEIROS COLOCADOS'))
print('-'*60)
print(campeonato[:5])
print('-'*60)
print('{:^60}'.format('4 ÚLTIMOS COLOCADOS'))
print('-'*60)
print(campeonato[-4:])
print('-'*60)
print('{:^60}'.format('EM ORDEM ALFABÉTICA'))
print('-'*60)
print(sorted(campeonato))
print('-'*60)
print('{:^60}'.format('COLOCAÇÃO DO INTERNACIONAL'))
print('-'*60)
print('O Internacional está em {}ª colocação.'.format(campeonato.index('Internacional')+1))
print('{:-^60}'.format('FIM DO PROGRAMA'))