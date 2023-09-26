
class Zoologico:

    _zonas = []

    def __init__(self, nombre, ubicacion) -> None:
        
        self._nombre = nombre
        self._ubicacion = ubicacion
    
    def agregarZonas(self, zona):

        Zoologico._zonas.append(zona)

    def cantidadAnimales(self):

        return len(Zoologico._zonas)