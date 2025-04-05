# Crie uma lista contendo seis frutas de sua escolha. 
# Depois de ter a lista pronta, converta essa lista em uma tupla. 
# Por fim, exiba o conteúdo da tupla resultante para verificar as frutas que foram armazenadas.

list_frut = ["banana", "uva", "morango", "manga", "graviola", "laranja"]
# o * coloca os valores da lista para fora do [], convertendo em uma tupla
tuple_frut = (*list_frut,)

print(tuple_frut)
