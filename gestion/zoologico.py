
class Zoologico:

    _zonas = []

    def __init__(self, nombre, ubicacion) -> None:
        
        self._nombre = nombre
        self._ubicacion = ubicacion
    
    def agregarZonas(self, zona):

        Zoologico._zonas.append(zona)

    def cantidadTotalAnimales(self):

        x  = 0

        for i in Zoologico._zonas:

            x += i.cantidadAnimales()

        return x

    
    def setNombre(self, listado):

        self._nombre = listado
    
    def getNombre(self):

        return  self._nombre
    
    def setUbicacion(self, x):

        self._ubicacion = x
    
    def getUbicacion(self):

        return  self._ubicacion
    
    def setZona(self, x):

        self._zonas= x
    
    def getZona(self):

        return  self._zonas