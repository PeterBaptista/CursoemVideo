# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
# cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de
# Zero, o dicionário receberá também o ano de contratação e o salário. Calcule

nome = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
carteira = int(input('Carteira de Trabalho[0 = não tem}]: '))
contratacao = salario = aposentadoria = 0
if carteira != 0:
    contratacao = int(input('Ano de contratação: '))
    salario = int(input('Salário: R$'))
    aposentadoria = contratacao + 36
cadastro = {"nome": nome,
            "nascimento": nascimento,
            "idade": (2021 - nascimento),
            "carteira": carteira,
            "Ano de contratação": contratacao,
            "salario": f'R${salario}',
            "Aposentadoria": f'em {aposentadoria}'}
for k, v in cadastro.items():
    print(f'{k} é {v}')


