def time_converter(t):
    return t * 3600


t = int(input('Informe a quantidade de horas: '))

print('{} hora(s) em segundos são {}s'.format(t, time_converter(t)))
