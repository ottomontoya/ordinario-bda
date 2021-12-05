from pymongo import results
from Monomio import Monomio
from random import randint, uniform

# TODO:
# prop grado
# finish agregar
# meth obtener (check guia)

class Polinomio:

    def __init__(self):
        self.__monomios = []
        self.__monomios.append(Monomio())

    @property
    def to_database(self):
        dict = {}
        dict['type'] = "Polinomio"
        dict['monomios'] = [m.to_database for m in self.__monomios]
        return dict

    # FALTA GARANTIZAR LO DE QUE SOLO HAYA UN POLINOMIO CON CADA EXPONENTE
    def agregar(self, monomio):
        self.__monomios.append(monomio)

    # Evaluate in regresion forms within the array list
    def evaluar(self, valor):
        resultado = 0
        for monomio in self.__monomios:
            resultado += monomio.evaluar(valor)
        return resultado

    # generate a unique polynomial
    def generatePoli(self):
        p = Polinomio()
        NumPoli = randint(2, 10)
        for i in range(NumPoli):
            coef = uniform(-1000, 1000)
            exp = randint(0, 500)
            p.agregar(Monomio(coef, exp))
        NumPoli = 0
        return p

    # Set the new representation form
    def __repr__(self):
        resultado = ""
        for monomio in self.__monomios:
            resultado += "+ " + str(monomio)
        return resultado
