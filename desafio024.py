#Crie um programa que leia o nome de uma cidade e diga se ela começa com o nome "SANTO".

cidade = input("Informe o nome da cidade: ").upper().strip()
#padrao = cidade.upper()
result = cidade[:5]
if result == 'SANTO':
    print('O nome da cidade começa com SANTO')
else:
    print('O nome da cidade não começa com SANTO')
