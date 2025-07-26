#POO Poliformismo

class Veiculo:
    def movimentar(self):
        return 'Veículo está em movimento.'
    

class Carro(Veiculo):
    def movimentar(self):
        return 'Carro está dirigindo.'

class Moto(Veiculo):
    def movimentar(self):
        return 'Moto está acelerando.'


objVeiculo = Veiculo().movimentar()
objCarro = Carro().movimentar()
objMoto = Moto().movimentar()

print(
    f'''
        Veiculo --> {objVeiculo}
        Carro --> {objCarro}
        Moto --> {objMoto}
    '''
)
