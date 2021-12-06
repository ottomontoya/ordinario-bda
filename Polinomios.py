import random
import pymongo
from Polinomio import Polinomio

URL = 'mongodb://ipy849:amerida@bdaordinario-shard-00-00.cn3bg.mongodb.net:27017,bdaordinario-shard-00-01.cn3bg.mongodb.net:27017,bdaordinario-shard-00-02.cn3bg.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-126nu3-shard-0&authSource=admin&retryWrites=true&w=majority'
DB_NAME = 'BDA'

def Generate():
    client = pymongo.MongoClient(URL)
    db = client[DB_NAME]
    cantidad_inserciones = random.randint(50000, 75000)
    db.algebra.insert_many([Polinomio.generate().to_database for _ in range(cantidad_inserciones)])

if __name__ == '__main__':
    Generate()