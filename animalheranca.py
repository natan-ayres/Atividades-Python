class Animal:
    def __init__(self, nome, raca, cor):
        self.nome = nome
        self.raca = raca
        self.cor = cor

    def corAnimal(self):
        self.raca = (f'{self.raca} {self.cor}')
        return self.raca
    
    def __str__(self):
            return f'Nome: {self.nome} Raça: {self.raca}'

class Cachorro(Animal):
    def som(self):
        return 'Woof Woof'
    
class Gato(Animal):
    def som(self):
        return 'Miau'

    
    
cachorro = Cachorro('Lobão', 'Vira-lata', 'Caramelo')
print(cachorro)
cachorro.corAnimal()
print(cachorro)
print(cachorro.som())
gato = Gato('Milky', 'Vira-lata', 'Branco')
print(gato)
gato.corAnimal()
print(gato)
print(gato.som())




    
    
 