class Carro:

    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome
    
    
fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1 = Motor('Motor 1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)
uno = Carro('Uno')
fiat = Fabricante('Fiat')
motor_2 = Motor('Motor 2.0')
uno.fabricante = fiat
uno.motor = motor_1
print(uno.nome, uno.fabricante.nome, uno.motor.nome)
toro = Carro('Toro')
toro.fabricante = fiat
toro.motor = motor_2
print(toro.nome, toro.fabricante.nome, toro.motor.nome)
