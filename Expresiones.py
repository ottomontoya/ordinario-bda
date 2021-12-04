from Polinomios import Polinomio
from random import randint, uniform


class Expresiones:

    # Constructor instance
    def __init__(self, operador1=None, operador2=None):
        if(operador1 == None):
            self.__operador1 = Polinomio().generatePoli()
        if(operador2 == None):
            self.__operador2 = Polinomio().generatePoli()
        self.__operacion = ""
        self.__resultado = ""

    # Set doc property
    @property
    def doc(self):
        dict = {}
        dict['type'] = "Expresion"
        dict['operacion'] = self.__operacion
        dict['operador1'] = self.__operador1.doc
        dict['operador2'] = self.__operador2.doc
        dict['resultado'] = self.__resultado
        return dict

    # Operation methods
    def mult(self, p1, p2):
        return p1 * p2

    def suma(self, p1, p2):
        return p1 + p2

    def resta(self, p1, p2):
        return p1 - p2

    def div(self, p1, p2):
        return p1 / p2

    # Evaluate and set values for the polinoms
    def evaluacion(self, valor):
        Poly1 = self.__operador1.evaluar(valor)
        Poly2 = self.__operador2.evaluar(valor)
        op = randint(1, 4)
        if(op == 1):
            self.__operacion = "suma"
            res = self.suma(Poly1, Poly2)
            self.__resultado = res
        if(op == 2):
            self.__operacion = "resta"
            res = self.resta(Poly1, Poly2)
            self.__resultado = res
        if(op == 3):
            self.__operacion = "division"
            res = self.div(Poly1, Poly2)
            self.__resultado = res
        if(op == 4):
            self.__operacion = "multiplicacion"
            res = self.mult(Poly1, Poly2)
            self.__resultado = res
