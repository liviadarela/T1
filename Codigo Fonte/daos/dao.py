import pickle
from abc import ABC, abstractmethod

#classe dao obstrata
class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {} #subtitui a lista que estava no controlador
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource,'rb'))

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()  #atualiza o arquivo quando um objeto for adicionado

    def update(self, key, obj):
        try: 
            if(self.__cache[key] != None):
                self.__cache[key] = obj 
                self.__dump()  
        except KeyError:
            pass  

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            pass 

    #remover um objeto
    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump() #atualiza o arquivo 
        except KeyError:
            pass 

    def get_all(self):
        return self.__cache.values()