from gestion.zoologico import Zoologico 

class Zona:

    _animales = []

    def __init__ (self, nombre, zoo):

        self._nombre = nombre
        self._zoo = zoo

    def agregarAnimales(self, animal):

        Zona._animales.append(self, animal)

    def cantidadAnimales(self):

        return len(Zona._animales)



