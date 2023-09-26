from zooAnimales.animal import Animal

class Ave (Animal):

    halcones = 0

    aguilas = 0

    _listado = []

    def __init__(self, nombre, edad, habitat, genero, colorPlumas) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

        
    @classmethod
    def cantidadAves(self):

        return len(Ave._listado)
    

    @classmethod
    def crearHalcon(self,  nombre, edad, genero):

        halcon = Ave( nombre, edad, "montanas", genero, "“cafe glorioso”")

        Ave.halcones += 1

        return halcon
    

    @classmethod
    def crearAguila(self,  nombre, edad, genero):

        aguila = Ave( nombre, edad, "montanas", genero, "blanco y amarrillo")

        Ave.aguilas += 1

        return aguila
    
    def listadoGetter():

        pass

    def setListado(self, listado):

        Ave._listado = listado
    
    def getListado(self):

        return  Ave._listado
    
    def setColorPlumas(self, x):

        self._colorPlumas = x
    
    def getColorPlumas(self):

        return  self._colorPlumas
    
   

    