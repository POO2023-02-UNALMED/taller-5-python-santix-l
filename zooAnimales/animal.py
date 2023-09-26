from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
from gestion.zona import Zona

class Animal:

    _totalAnimales = 0
    
    def __init__(self, nombre, edad, habitat, genero) -> None:
        
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        _zona = None

    
    
    def totalPorTipo(self):

        return "Mamiferos: "+ Mamifero.cantidadMamiferos()+ "\nAves: "+Ave.cantidadAves()+ "\nReptiles: "+Reptil.cantidadReptiles()+ "\nPeces: "+ Pez.cantidadPeces()+ "\nAnfibios: " + Anfibio.cantidadAnfibios()

    def __str__(self):
       
       if self._zona != None:

        return "Mi nombre es "+self._nombre+", tengo una edad de "+self._edad+", habito en "+self._habitat+" y mi genero es "+ self._genero +", la zona en la que me ubico es " + self._zona +", en el " + self._zona.getZoo()
       
       else:
          
          return "Mi nombre es "+self._nombre+", tengo una edad de "+self._edad+", habito en "+self._habitat+" y mi genero es "+ self._genero
       
    
    def setNombre(self, listado):

        self._nombre = listado
    
    def getNombre(self):

        return  self._nombre
    
    def setEdad(self, x):

        self._edad = x
    
    def getEdad(self):

        return  self._edad
    
    def setHabitat(self, x):

        self._habitat = x
    
    def getHabitat(self):

        return  self._habitat
    
    def setGenero(self, x):

        self._genero = x
    
    def getGenero(self):

        return  self._genero
    
    @classmethod
    def setTotalAnimales(self, x):

        Animal._totalAnimales = x
    
    @classmethod
    def getTotalAnimales(self):

        return  Animal._totalAnimales
    
    def setZona(self, x):

        self._zona = x
    
    def getZona(self):

        return  self._zona
    
    

