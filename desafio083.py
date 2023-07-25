'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

'''expressao = str(input('Informe a expressão: '))
parenteses_esquerda = expressao.count('(')
parenteses_direita = expressao.count(')')
if parenteses_esquerda == parenteses_direita:
    print('Expressão válida')
else:
    print('Expressão inválida')'''

expressao = str(input('Informe a expressão: '))
pilha = []
for i in expressao:
    if i == '(':
        pilha.append('(')
    elif i == ')':
        if len(expressao) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão válida.')
else:
    print('Expressão inválida.')
