#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. o programa vai perguntar o
# valor da casa, o salário do comprador e quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salaário ou então o empréstimo será negado.

valor_casa = float(input('Qual o valor do imóvel? '))
salario_comprador = float(input('Informe o salário: '))
tempo_financimamento = int(input('Em quantos meses deseja financiar: '))

valor_financiamento = valor_casa / tempo_financimamento

if valor_financiamento > (salario_comprador * 0.3):
    print('O valor da parcela mensal {:.2f} não pode exceder 30% do valor do seu salário'.format(valor_financiamento))
    print('Empréstimo NEGADO')
else:
    print('O valor da prestação mensal será de R$ {:.2f}'.format(valor_financiamento))