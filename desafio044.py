#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
#pagamento:
#à vista dinheiro / cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

preco = float(input('Informe o preço: '))
condicao_pagamento = int(input('Informe a condição de pagamento: \n1. À vista no dinheiro ou cheque\n2. À vista no cartão\n3. Em até 2x no cartão\n4. 3x no cartão\n'))
if condicao_pagamento == 1:
    print('Preço com 10% de desconto: R$ {:.2f}'.format(preco - (preco * 0.1)))
elif condicao_pagamento == 2:
    print('Preço com 5% de desconto: R$ {:.2f}'.format(preco - (preco * 0.05)))
elif condicao_pagamento == 3:
    print('Preço de R$ {:.2f} em duas vezes sem juros - 2x: R$ {:.2f}'.format(preco, preco/2))
else:
    parcelas = int(input('Em quantas vezes deseja parcelar: '))
    print('Preço com 20% de juros: R$ {:.2f} fica {:.2f} em {}x'.format(preco * 1.20, (preco * 1.20 / parcelas), parcelas))
