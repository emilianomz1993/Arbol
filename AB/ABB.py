
from pickle import FALSE
from Nodo import Nodo

class abb:
    __raiz=Nodo
    
    def vacia(self,raiz):
        return raiz.getelem==None
    
    def getraiz(self):
        return self.__raiz
    
    def set(self,elemento,raiz):
        aux=raiz
        if raiz.vacia(raiz):
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
        if self.vacia(raiz):
            return False
        elif raiz.getelem()==elemento:
            return raiz
        elif elemento<raiz.getelem():
            self.search(elemento,raiz.getsigiz())
        elif elemento>raiz.gerelem():
            self.search(elemento,raiz.getsigde())

    def level(self,elemento,raiz,contador):
        if self.vacia(raiz):
            contador=0
            return contador
        elif raiz.getelem()==elemento:
            return contador+1
        else:
            if raiz.getelem()>elemento:
                contador+=1
                self.level(elemento,raiz.getsigiz(),contador)
            else:
                contador+=1
                self.level(elemento,raiz.getsigde(),contador)

    def sheet(self,elemento,raiz):
        if self.vacia(raiz):
            return False
        elif raiz.getelem()==elemento:
            if raiz.getsigde().getelem()==None and raiz.getsigiz().getelem()==None:
                return True
            else:
                return False
        elif elemento<raiz.getelem():
            self.search(elemento,raiz.getsigiz())
        elif elemento>raiz.gerelem():
            self.search(elemento,raiz.getsigde())

    def son(self,hijo,padre):
        aux=self.search(padre,self.__raiz)
        if aux.getsigde().getelem()==hijo or aux.getsigiz().hijo
            return True
        else
            return False

    def father(self,hijo,padre):
        aux=self.search(padre,self.__raiz)
        if aux.getsigde().getelem()==hijo or aux.getsigiz().hijo
            return True
        else
            return False

    def inorden(self, nodo):

        if nodo is not None:
            self.inorden(nodo.getsigiz)
            print(nodo.getelem, end=", ")
            self.inorden(nodo.getsigde)

    def preorden(self, nodo):
        if nodo is not None:
            print(nodo.getelem, end=", ")
            self.preorden(nodo.getsigiz)
            self.__preorden_recursivo(nodo.getsigde)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.getsigiz)
            self.__postorden_recursivo(nodo.getsigde)
            print(nodo.getelem, end=", ")