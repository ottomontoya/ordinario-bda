import random
import pymongo
from Polinomio import Polinomio
from vars import *


def Generate():
    client = pymongo.MongoClient(URL)
    db = client[DB_NAME]
    cantidad_inserciones = random.randint(50000, 75000)
    db.algebra.insert_many([Polinomio.generate().to_database for _ in range(cantidad_inserciones)])

if __name__ == '__main__':
    Generate()