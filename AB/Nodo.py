class Nodo:
    __sigder=None
    __sigizq=None
    __elemento=int
    
    def __init__(self):
        self.__sigder=Nodo
        self.__sigizq=Nodo
        self.__elemento=None
        
    def setsigiz(self, elemento):
        self.__sigizq.setelemento(elemento)
        return
    
    def setsigde(self, elemento):
        self.__sigder.setelemento(elemento)
        return
    
    def setelemento(self, elemento):
        self.__elemento=elemento
        
    def getsigiz(self):
        return self.__sigizq
    
    def getsigde(self):
        return self.__sigder
    
    def getelem(self):
        return self.__elemento
