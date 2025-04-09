dictInfo = {}

name = str(input('Qual o seu nome? '))
dictInfo['nome'] = name

contact = str(input('Informe o número para contato: '))
dictInfo['telefone'] = contact

email = str(input('Qual o seu email? '))
dictInfo['email'] = email

print(f'Informações do usuário: {dictInfo}')


