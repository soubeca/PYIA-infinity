def maior_numero(*args):
  maior = args[0]
  for number in args:
    if maior < number:
      maior = number
  return maior

print(maior_numero(5,2,8))


