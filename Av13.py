#Atividade POO III

class ContaBancaria():
    
    def __init__(self, saldo, titular):
        self.__saldo = saldo
        self.__titular = titular
        
    def depositar(self, valor):
        self.__saldo += valor
        
    def sacar(self, valor):
        if not (valor <= self.__saldo and valor > 0):
            return 'Saldo insuficiente.'
        
        self.__saldo -= valor
    
    def exibirSaldo(self):
        return self.__saldo
    
    def getTitular(self):
        return self.__titular
    
objContaBancaria = ContaBancaria(50, "Rebeca")
print("A conta bancaria da cliente: ", objContaBancaria.getTitular(), objContaBancaria.exibirSaldo())
objContaBancaria.sacar(20)
print("A conta bancaria da cliente: ", objContaBancaria.getTitular(), objContaBancaria.exibirSaldo())
objContaBancaria.depositar(70)
print("A conta bancaria da cliente: ", objContaBancaria.getTitular(), objContaBancaria.exibirSaldo())
