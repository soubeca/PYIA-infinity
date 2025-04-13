purchases = {}
total = 0

while True:
  print('''
  ________________ Escolha o número da opção que deseja realizar: _______________
  1. Criar Lista de compras
  2. Calcular preço das compras
  3. Sair
  ________________________________________________________________________________
  ''')

  resp = int(input('informe a opção: '))

  if resp == 1:
    product = str(input('Informe o nome do produto: '))
    precing = float(input('Informe o preço: '))
  
    purchases[product] = precing
    print(purchases)
  elif resp == 2:
    for precingProduct in purchases.values():
      total += precingProduct
    print(f'O valor total da compra é R${total:.2f}')
  else:
    print('Volte sempre ☺️!')
    break
   
  
