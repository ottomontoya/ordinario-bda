from Polinomios import Polinomio
from random import randint, uniform

# TODO: please check
# operation methods needed?
# evaluacion needed?

class Expresiones:

    def __init__(self, operando1 = None, operando2 = None):
        self.__operando1 = operando1
        self.__operando2 = operando2

        if operando1 is None:
            self.__operador1 = Polinomio().generatePoli()
        if operando2 is None:
            self.__operador2 = Polinomio().generatePoli()

        self.__operacion = ""
        self.__resultado = ""

    @property
    def operando1(self):
        return self.__operando1

    @property
    def operando2(self):
        return self.__operando2

    @property
    def to_database(self):
        dict = {}
        dict['type'] = "Expresion"
        dict['operacion'] = self.__operacion
        dict['operando1'] = self.__operando1.doc
        dict['operando2'] = self.__operando2.doc
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
        Poly1 = self.__operando1.evaluar(valor)
        Poly2 = self.__operando2.evaluar(valor)
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
