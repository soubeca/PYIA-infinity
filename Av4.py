def media(value1,value2,value3):
  '''
    A função tem o objetivo de tirar a média aritimética dos valores inseridos.
  '''
  return (value1 + value2 + value3)/3

value1 = float(input('Informe a primeira nota: '))
value2 = float(input('Informe a segunda nota: '))
value3 = float(input('Informe a terceira nota: '))

resultado = f'A média aritimética é = {media(value1,value2,value3):.2f}'

print (resultado)
