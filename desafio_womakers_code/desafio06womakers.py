def conversor_temperatura(temperatura):
    f = ((9 * temperatura + 160)/5)
    return f


temperatura = float(input('Informe a temperatura em Cº: '))
conversao = conversor_temperatura(temperatura)
print('{}ºC são {:.1f}ºF'.format(temperatura, conversao))
