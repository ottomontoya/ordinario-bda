
import random
import pymongo
from Monomio import Monomio
from Polinomio import Polinomio

URL = 'mongodb://ipy849:amerida@bdaordinario-shard-00-00.cn3bg.mongodb.net:27017,bdaordinario-shard-00-01.cn3bg.mongodb.net:27017,bdaordinario-shard-00-02.cn3bg.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-126nu3-shard-0&authSource=admin&retryWrites=true&w=majority'
DB_NAME = 'BDA'

class Expresion:

    # Constructor
    def __init__(self, operador, operando1, operando2):
        if operador not in ['+', '-', '*', '/']:
            raise Exception('Operación/Operador inválido')
        for i in operando1, operando2:
            if not isinstance(i, Monomio) and not isinstance(i, Polinomio):
                raise Exception('Los operandos deber ser una instancia de Monomio o Polinimio')
        self.__operador = operador
        self.__operando1 = operando1
        self.__operando2 = operando2

    # Propiedades
    @property
    def operacion(self):
        return self.__operador

    @property
    def operando1(self):
        return self.__operando1

    @property
    def operando2(self):
        return self.__operando2

    @property
    def to_database(self):
        obj = dict()
        obj['operacion'] = self.__operador
        obj['operando1'] = self.__operando1.to_database
        obj['operando2'] = self.__operando2.to_database
        return obj

    # Métodos
    def evaluacion(self, value):
        '''Evalua la expresion'''
        return eval(f'{self.__operando1.evaluar(value)} {self.operacion} {self.__operando2.evaluar(value)}')
    
    @staticmethod
    def generate(operacion):
        operando1 = None
        if random.random() > .5:
            operando1 = Polinomio.generate()
        else:
            operando1 = Monomio.generate()

        operando2 = None
        if random.random() > .5:
            operando2 = Polinomio.generate()
        else:
            operando2 = Monomio.generate()

        return Expresion(operacion, operando1, operando2)

    # Dunder methods
    def __repr__(self):
        '''Representación'''
        return f'({self.__operando1}) {self.operacion} ({self.__operando2})'

def Generate():
    client = pymongo.MongoClient(URL)
    db = client[DB_NAME]
    cantidad_inserciones = random.randint(33000, 77000)
    inserciones = list()
    operaciones = ['+', '-', '*', '/']
    for i in range(cantidad_inserciones):
        operacion = operaciones[i % 4]
        inserciones.append(Expresion.generate(operacion).to_database)
    db.algebra.insert_many(inserciones)

if __name__ == '__main__':
    Generate()