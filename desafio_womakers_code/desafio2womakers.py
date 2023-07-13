def classifica_idade(idade):
    if idade < 0:
        return 'Idade inválida'
    elif idade <= 12:
        return 'Criança - 0 a 12 anos'
    elif idade <= 17:
        return 'Adolescente - 13 a 17 anos'
    else:
        return 'Adulto - acima de 18 anos'


idade = int(input('Informe sua idade: '))

print(classifica_idade(idade))
