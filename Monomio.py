import random
import pymongo

URL = 'mongodb://ipy849:amerida@bdaordinario-shard-00-00.cn3bg.mongodb.net:27017,bdaordinario-shard-00-01.cn3bg.mongodb.net:27017,bdaordinario-shard-00-02.cn3bg.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-126nu3-shard-0&authSource=admin&retryWrites=true&w=majority'
DB_NAME = 'BDA'

class Monomio:

    # Constructor
    def __init__(self, coeficiente=0, exponente=0):
        if exponente < 0:
            raise Exception('El exponente no debe ser negativo')
        self.__coeficiente = coeficiente
        self.__exponente = exponente

    # Propiedades
    @property
    def coeficiente(self):
        return self.__coeficiente

    @property
    def exponente(self):
        return self.__exponente

    @property
    def to_database(self):
        obj = dict()
        obj['type'] = "Monomio"
        obj['coeficiente'] = self.__coeficiente
        obj['exponente'] = self.__exponente
        return obj

    # Métodos
    def evaluar(self, valor):
        '''Evalúa a la instacia de Monomio'''
        return self.__coeficiente * (valor ** self.__exponente)

    def sumar(self, monomio):
        '''Suma dos monomios'''
        return self + monomio
    
    def restar(self, monomio):
        '''Resta dos monomios'''
        return self - monomio
    
    @staticmethod
    def generate():
        coeficiente = round((random.random() * 50) - 25, 2)
        exponente = random.randint(0, 15)
        return Monomio(coeficiente, exponente)

    # Dunder methods
    def __str__(self):
        '''Representación str'''
        return f"{self.__coeficiente} x^{self.__exponente}"
    
    def __repr__(self):
        '''Representación str'''
        return str(self)

    def __add__(self, value):
        '''Habilitar y definir operador suma'''
        if not isinstance(value, Monomio) or self.__exponente != value.__exponente:
            raise Exception('Una instancia de Monomio solo puede operar con otro Monomio con el mismo exponente')
        return Monomio(self.__coeficiente + value.__coeficiente, self.__exponente)

    def __sub__(self, value):
        '''Habilitar y definir operador substracción'''
        if not isinstance(value, Monomio) or self.__exponente != value.__exponente:
            raise Exception('Una instancia de Monomio solo puede operar con otro Monomio con el mismo exponente')
        return Monomio(self.__coeficiente - value.__coeficiente, self.exponente)


def Generate():
    client = pymongo.MongoClient(URL)
    db = client[DB_NAME]
    cantidad_inserciones = random.randint(30000, 50000)
    db.algebra.insert_many([Monomio.generate().to_database for _ in range(cantidad_inserciones)])

if __name__ == '__main__':
    Generate()