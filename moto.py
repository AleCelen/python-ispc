# esto es una moto en poo
class Moto:
    num_ruedas = 2

    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    # Metodos para mostrar datos
    def get_marca(self):
        marca = 'Nueva marca'
        print(self.marca)

    # Metodo para acelerar
    def acelerar(self, km):
        print('acelerando {0} km'.format(km))


# intanciar objeto
bmw_r1000 = Moto(marca='BMW', modelo='R1000', color='blanca')
suzuki_gsx = Moto('Suzuki', 'gsx', 'negra')
moto3 = Moto('Zanella', 'Patagonia150', 'verde')
print(bmw_r1000.marca, bmw_r1000.modelo, bmw_r1000.color)
# Uso metodo acelerar
bmw_r1000.acelerar(20)

#variable de clase
bmw_r1000.num_ruedas = 3
print(bmw_r1000.num_ruedas)

# Nota:
# Este decorador o decorator es, básicamente, un modificador que permite ejecutar una
# versión modificada o decorada de una función o método concreto.
# Supongamos que tenemos una clase que representa un circulo y deseamos tener un
# atributo que se refiera al área de mismo. Dado que esta área puede ser calculada en
# función del radio del circulo, parece lógico utilizar property para llevar a cabo el
# procesamiento requerido.
from math import pi


class circle:
    def __init__(self, radio):

        self.radio = radio
    @property
    def area(self):
        return pi * (self.radio ** 2)
c = circle(25)
print(c.area)