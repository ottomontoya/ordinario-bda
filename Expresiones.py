import random
import pymongo
from Monomio import Monomio
from Polinomio import Polinomio
from Expresion import Expresion
from vars import *

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