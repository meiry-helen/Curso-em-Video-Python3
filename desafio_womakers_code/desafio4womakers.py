def calcula_media(M1, M2, M3):
    media = (M1 + M2 + M3)/3
    if media >= 0 and media <= 4.0:
        return 'Reprovado!'
    elif media <= 6.0:
        exame = float(input('Aluno de exame!\nIndique a nota do exame: '))
        if exame > 6.0:
            return 'Aprovado!'
        else:
            return 'Reprovado!'
    elif media <= 10:
        return 'Aprovado!'


M1 = float(input('Informe a nota 1: '))
M2 = float(input('Informe a nota 2: '))
M3 = float(input('Informe a nota 3: '))
resultado = calcula_media(M1, M2, M3)
print('Situação do aluno: ', resultado)
