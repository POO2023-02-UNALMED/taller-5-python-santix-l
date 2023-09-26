from zooAnimales.animal import Animal

class Anfibio (Animal):

    ranas = 0

    salamandras = 0

    _listado = []

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    
    @classmethod
    def cantidadAnfibios(self):

        return len(Anfibio._listado)
    

    @classmethod
    def crearRana(self,  nombre, edad, genero):

        rana = Anfibio( nombre, edad, "selva", genero, "rojo", True)

        Anfibio.ranas += 1

        return rana
    

    @classmethod
    def crearSalamandras(self,  nombre, edad, genero):

        salamandra = Anfibio( nombre, edad, "selva", genero, "negro y amarillo", False)

        Anfibio.salamandras += 1

        return salamandra
    
    def setListado(self, listado):

        Anfibio._listado = listado
    
    def getListado(self):

        return  Anfibio._listado
    
    def setColorPiel(self, x):

        self._colorPiel = x
    
    def getColorPiel(self):

        return  self._colorPiel
    
    def setVenenoso(self, x):

        self._venenoso = x
    
    def getVenenoso(self):

        return  self._venenoso
