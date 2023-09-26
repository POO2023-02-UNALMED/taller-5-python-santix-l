from typing import Any
from zooAnimales.animal import Animal

class Pez (Animal):

    salmones = 0

    bacalaos = 0

    _listado = []

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    
    @classmethod
    def cantidadPeces(self):

        return len(Pez._listado)
    

    @classmethod
    def crearSalmon(self,  nombre, edad, genero):

        salmon = Pez( nombre, edad, "oceano", genero, "rojo", 6)

        Pez.salmones += 1

        return salmon
    

    @classmethod
    def crearBacalao(self,  nombre, edad, genero):

        bacalao = Pez( nombre, edad, "oceano", genero, "gris", 6)

        Pez.bacalaos += 1

        return bacalao
    
    def setListado(self, listado):

        Pez._listado = listado
    
    def getListado(self):

        return  Pez._listado
    
    def setColorEscamas(self, x):

        self._colorEscamas = x
    
    def getColorEscamas(self):

        return  self._colorEscamas
    
    def setCantidadAletas(self, x):

        self._cantidadAletas = x
    
    def getCantidadAletas(self):

        return  self._cantidadAletas
