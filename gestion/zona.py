
class Zona:

    _animales = []

    def __init__ (self, nombre, zoo = None):

        self._nombre = nombre
        self._zoo = zoo

    def agregarAnimales(self, animal):

        Zona._animales.append(animal)

    def cantidadAnimales(self):

        return len(Zona._animales)
    
    def setNombre(self, listado):

        self._nombre = listado
    
    def getNombre(self):

        return  self._nombre
    
    def setZoo(self, x):

        self._zoo = x
    
    def getZoo(self):

        return  self._zoo



