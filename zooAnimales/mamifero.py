from zooAnimales.animal import Animal

class Mamifero (Animal):

    caballos = 0

    leones = 0

    _listado = []

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    @classmethod
    def cantidadMamiferos(self):

        return len(Mamifero._listado)


    @classmethod
    def crearCaballo(self,  nombre, edad, genero):

        caballo = Mamifero( nombre, edad, "pradera", genero, True, 4)

        Mamifero.caballos += 1

        return caballo


    @classmethod
    def crearLeon(self,  nombre, edad, genero):

        leon = Mamifero( nombre, edad, "selva", genero, True, 4)

        Mamifero.leones += 1

        return leon
    
    def setListado(self, listado):

        Mamifero._listado = listado
    
    def getListado(self):

        return  Mamifero._listado
    
    def setPelaje(self, x):

        self._pelaje = x
    
    def isPelaje(self):

        return  self._pelaje
    
    def setPatas(self, x):

        self._patas = x
    
    def getPatas(self):

        return  self._patas


