class Animal:
    def falar(self):
        print('Este animal faz um som genérico.')

class Cachorro:
    def falar(self):
        print('O cachorro está latindo.🐶')

class Gato:
    def falar(self):
        print('O gato está miando.')

objAnimal = Animal().falar()
objCachorro = Cachorro().falar()
objGato = Gato().falar()
