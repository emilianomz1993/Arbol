from pickle import FALSE
from Nodo import Nodo

class abb:
    __raiz=Nodo
    
    def vacia(self):
        return self.__raiz.getelem==None
    
    def getraiz(self):
        return self.__raiz
    
    def set(self,elemento,raiz):
        aux=raiz
        if raiz.vacia():
            aux.getelem(elemento)
        elif elemento<aux.getelem():
            if aux.getsigiz()==None:                
                aux.setsigiz(elemento)
            else:
                self.set(elemento,aux.getsigiz())
        elif elemento>aux.getelem():
            if aux.getsigde()==None:                
                aux.setsigde(elemento)
            else:
                self.set(elemento,aux.getsigde())
        return
    
    def search(self,elemento,raiz):
        if self.vacia():
            return False
        elif raiz.getelem()==elemento:
            return True
        elif elemento<raiz.getelem():
            self.search(elemento,raiz.getsigiz())
        elif elemento>raiz.gerelem():
            self.search(elemento,raiz.getsigde())
    def level(self,elemento,raiz):
        if self.vacia():
            return 0
        elif raiz.getelem()==elemento:
            return True
        elif elemento<raiz.getelem():
            self.search(elemento,raiz.getsigiz())
        elif elemento>raiz.gerelem():
            self.search(elemento,raiz.getsigde())
            