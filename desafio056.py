#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final, mostre:
#-- A média de idade do grupo
#-- Qual o nome do homem mais velho
#-- Quantas mulheres têm menos de 20 anos
soma_idade = 0
qtd_mulheres = 0
idade_m_maior = 0
nome_m = ''
for c in range(1, 5):
    print('-'*5, c, '-'*5)
    nome = input('Informe o nome: ').strip()
    idade = float(input('Informe a idade: '))
    sexo = int(input('[1] Feminino\n[2] Masculino\n'))

    #cálculo da idade média do grupo
    soma_idade += idade
    media_idade = soma_idade / c

    #quantas mulheres têm menos de 20 anos
    if sexo == 1 and idade < 20:
       qtd_mulheres += 1

    #qual o nome do homem mais velho
    if sexo == 2 and idade > idade_m_maior:
        idade_m_maior = idade
        nome_m = nome

print('A média das idades informadas é de {:.2f}'.format(media_idade))
print('A quantidade de mulheres com menos de 20 anos é de {}'.format(qtd_mulheres))
print('O nome do homem mais velho é {}'.format(nome_m))
