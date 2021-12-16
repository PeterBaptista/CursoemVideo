import time
nome = str(input('Qual é seu nome? ')).strip()

if nome.upper() == 'PEDRO':
    print('Que nome bonito!')
elif nome.upper() == 'JOÃO' or nome.upper() == 'MARIA' or nome.upper() == 'ENZO':
    print('Seu nome é bem popular no Brasil')
elif nome.lower() in 'ana júlia débora elda ellen sofia giovanna patrícia':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal...')
time.sleep(1.5)
print('Tenha um bom dia, {}!'.format(nome.capitalize()))

