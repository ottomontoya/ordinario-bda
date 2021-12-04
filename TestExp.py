from Expresiones import Expresiones
# Mongo Imports
import pymongo
import pprint
import bson.objectid

# Conect to the Atlas UI Cluster
client = pymongo.MongoClient("XXX")
db = XXX

"""
p = Polinomio()
print(p.generatePoli())
"""
op1 = Expresiones()
res = op1.evaluacion(2)
print(op1.doc)
db.exp.insert_one(op1.doc)
