from Expresiones import Expresiones
from Filters import Filters
from Monomio import Monomio
from Polinomios import Polinomio
from random import randint, uniform
# Mongo Imports
import pymongo
import pprint
import bson.objectid


class Principal:

    # Metodo para generar 100 monomios (documentos)
    def generateMononomiosDB(self):
        # Monomios
        # Ciclo para crear 100 monomios
        monomiosL = []
        for i in range(100):
            coef = uniform(-1000, 1000)
            exp = randint(0, 5000)
            monomiosL.append(Monomio(coef, exp))
        # Insertar en la base de de datos (monomios)
        for monomio in monomiosL:
            bypass_validation = False
            db.algebraTest.insert_one(monomio.doc, bypass_validation)
        print("Insercion de Monomios correcta")

    # Metodo para generar 100 polinomios (documentos)
    def generatePolinomiosDB(self):
        # Polinomio
        for i in range(100):
            p = Polinomio()
            NumPoli = randint(2, 10)
            for j in range(NumPoli):
                coef = uniform(-1000, 1000)
                exp = randint(0, 5000)
                p.add(Monomio(coef, exp))
            db.algebraTest.insert_one(p.doc)
            NumPoli = 0
        # Mensaje de confirmacion en consola
        print("Insercion de Polinomios correcta")

    # Metodo para generar 100 expresiones (documentos)
    def generateExpresionesDB(self):
        # Polinomio
        for i in range(100):
            e = Expresiones()
            value = randint(2, 4)
            e.evaluacion(value)
            db.algebraTest.insert_one(e.doc)
            value = 0
        # Mensaje de confirmacion en consola
        print("Insercion de Expresiones correcta")

    # Metodo para llamara a los filtros de busqueda en MongoDB
    def filters(self):
        f = Filters()
        # f.ExpGte650()
        # f.PoliCoefGte100Lte400()
        # f.TypeMonomioCoefGte400()
        f.TypePoliArrayIs5()


if __name__ == "__main__":
    # Conect to the Atlas UI Cluster
    client = pymongo.MongoClient("XXX")
    db = XXX
    # Calling Methods
    m = Principal()
    # m.generateMononomiosDB()
    # m.generatePolinomiosDB()
    m.generateExpresionesDB()
    # print(m.filters())
