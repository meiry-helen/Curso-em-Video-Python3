import emoji

print(emoji.emojize('Hello, World :sunglasses:', language = 'alias'))

km = float(input('Quantos quilômetros foram percorridos: '))
d = int(input('Por quantos dias o carro foi alugado: '))

v_km = 0.15
v_d = 60.0

p = (d * v_d) + (km * v_km)
print('O valor a pagar é de R$ {:.2f}'.format(p))
