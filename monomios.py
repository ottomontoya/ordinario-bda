import random
import pymongo
from Monomio import Monomio
from vars import *

def Generate():
    client = pymongo.MongoClient(URL)
    db = client[DB_NAME]
    cantidad_inserciones = random.randint(30000, 50000)
    db.algebra.insert_many([Monomio.generate().to_database for _ in range(cantidad_inserciones)])

if __name__ == '__main__':
    Generate()