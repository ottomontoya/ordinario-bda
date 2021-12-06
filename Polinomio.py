import random
import pymongo
from Monomio import Monomio

URL = 'mongodb://ipy849:amerida@bdaordinario-shard-00-00.cn3bg.mongodb.net:27017,bdaordinario-shard-00-01.cn3bg.mongodb.net:27017,bdaordinario-shard-00-02.cn3bg.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-126nu3-shard-0&authSource=admin&retryWrites=true&w=majority'
DB_NAME = 'BDA'

class Polinomio:

    # Constructor
    def __init__(self):
        self.__monomios = []
        self.__monomios.append(Monomio())

    # Propiedades
    @property
    def monomios(self):
        return self.__monomios

    @property
    def grado(self):
        _grado = 0
        for monomio in self.__monomios:
            if _grado < monomio.exponente: 
                _grado = monomio.exponente
        return _grado

    @property
    def to_database(self):
        obj = dict()
        obj['type'] = "Polinomio"
        obj['grado'] = self.grado
        obj['length'] = len(self.monomios)
        obj['monomios'] = [m.to_database for m in self.__monomios]
        return obj

    # Métodos
    def agregar(self, monomio):
        '''Agrega un Monomio a la instancia de Polinomio y lo agrupa 
        con el resto de monomios en caso de ser posible'''
        if not isinstance(monomio, Monomio):
            raise Exception('Solo puedes agregar instancias de Monomio a una instancia de Polinomio')
        self.__monomios.append(monomio)
        self.__agrupar()

    def obtener(self, exponente):
        '''Obtiene una instancia de Monomio contenida en el Polinomio si
        esta existe
        @returns
            Monomio|None'''
        if exponente < 0:
            return None
        for monomio in self.__monomios:
            if monomio.exponente == exponente:
                return monomio
        return None

    # Evaluate in regresion forms within the array list
    def evaluar(self, valor):
        '''Evalúa todos los monomios y obtiene la suma de estos en la instancia de Polinomio'''
        resultado = 0
        for monomio in self.__monomios:
            resultado += monomio.evaluar(valor)
        return resultado

    def __agrupar(self):
        '''Agrupa los Monomios contenidos en la instancia de Polinomio'''
        for i in range(len(self.__monomios) - 1):
            for j in range(i+1, len(self.__monomios)):
                if self.__monomios[i].exponente < self.__monomios[j].exponente:
                    temp = self.__monomios[i]
                    self.__monomios[i] = self.__monomios[j]
                    self.__monomios[j] = temp
                elif self.__monomios[i].exponente == self.__monomios[j].exponente:
                    # No implementamos el dunder method __iadd__ y no podemos usar += pero si +
                    self.__monomios[i] =  self.__monomios[i] + self.__monomios.pop(j)

    @staticmethod
    def generate():
        polinomio = Polinomio()
        for _ in range(random.randint(1, 5)):
            polinomio.agregar(Monomio.generate())
        return polinomio

    # Dunder methods
    def __repr__(self):
        # No sé por qué razón no me deja usar un los __repr__ para representar la colección
        return ' + '.join([str(item) for item in self.__monomios])


def Generate():
    client = pymongo.MongoClient(URL)
    db = client[DB_NAME]
    cantidad_inserciones = random.randint(50000, 75000)
    db.algebra.insert_many([Polinomio.generate().to_database for _ in range(cantidad_inserciones)])

if __name__ == '__main__':
    Generate()