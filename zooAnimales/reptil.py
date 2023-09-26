from zooAnimales.animal import Animal

class Reptil (Animal):

    iguanas = 0

    serpientes = 0

    _listado = []

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    
    @classmethod
    def cantidadReptiles(self):

        return len(Reptil._listado)
    

    @classmethod
    def crearIguana(self,  nombre, edad, genero):

        serpiente = Reptil( nombre, edad, "humedal", genero, "verde", 3)

        Reptil.iguanas += 1

        return serpiente
    

    @classmethod
    def crearSerpiente(self,  nombre, edad, genero):

        serpiente = Reptil( nombre, edad, "jungla", genero, "blanco", 1)

        Reptil.serpientes += 1

        return serpiente

    def setListado(self, listado):

        Reptil._listado = listado
    
    def getListado(self):

        return  Reptil._listado
    
    def setColorEscamas(self, x):

        self._colorEscamas = x
    
    def getColorEscamas(self):

        return  self._colorEscamas
    
    def setLargoCola(self, x):

        self._largoCola = x
    
    def getLargoCola(self):

        return  self._largoCola
