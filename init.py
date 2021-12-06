import pymongo
from pymongo import database

URL = 'mongodb://ipy849:amerida@bdaordinario-shard-00-00.cn3bg.mongodb.net:27017,bdaordinario-shard-00-01.cn3bg.mongodb.net:27017,bdaordinario-shard-00-02.cn3bg.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-126nu3-shard-0&authSource=admin&retryWrites=true&w=majority'
DB_NAME = 'BDA'

def init_database():
    '''Funcion de inicio de la BD'''
    client = pymongo.MongoClient(URL)
    db = client[DB_NAME]
    if 'algebra' in db.list_collection_names():
        db.drop_collection('algebra')
    db.create_collection('algebra')


if __name__ == '__main__':
    init_database()