import random
import pymongo
from Monomio import Monomio
from Polinomio import Polinomio
from Expresion import Expresion

URL = 'mongodb://ipy849:amerida@bdaordinario-shard-00-00.cn3bg.mongodb.net:27017,bdaordinario-shard-00-01.cn3bg.mongodb.net:27017,bdaordinario-shard-00-02.cn3bg.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-126nu3-shard-0&authSource=admin&retryWrites=true&w=majority'
DB_NAME = 'BDA'

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