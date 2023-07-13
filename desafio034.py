#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superior a R$ 1250,00, calcule um aumento de 10%.
#Para salários inferiores, calcule um aumento de 15%.

salario = float(input('Informe seu salário: '))
if salario > 1250:
    print('Seu salário com aumento de 10% será de R$ {:.2f}'.format(salario * 1.10))
else:
    print('Seu salário com aumento de 15% será de R$ {:.2f}'.format(salario * 1.15))
