l = float(input('Qual a largura da parede? '))
a = float(input('Qual a altura da parede? '))
m2 = l * a
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(l, a, m2))
print('Você precisará de {:.2f} litros de tinta para pintar essa parede.'.format((l * a)/2))
