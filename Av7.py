#Crie uma função chamada lancar_dados que utilizará o módulo random para simular o lançamento de dois dados. 
#Cada dado deve gerar um número aleatório entre 1 e 6. 
#A função deve somar os resultados desses dois lançamentos e retornar o valor total.

def lancar_dados():
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    
    total = num1 + num2
    return (f'A soma entre os números aletórios {num1} e {num2} é {total}')

print (lancar_dados())

  


