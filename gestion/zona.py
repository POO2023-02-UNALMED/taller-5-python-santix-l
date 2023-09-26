
class Zona:

    

    def __init__ (self, nombre, zoo = None):

        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

    def agregarAnimales(self, animal):

        self._animales.append(animal)

    def cantidadAnimales(self):

        return len(self._animales)
    
    def setNombre(self, listado):

        self._nombre = listado
    
    def getNombre(self):

        return  self._nombre
    
    def setZoo(self, x):

        self._zoo = x
    
    def getZoo(self):

        return  self._zoo



