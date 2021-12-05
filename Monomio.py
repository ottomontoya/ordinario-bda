# TODO: meth sumar y restar (check guia)

class Monomio:

    # Constructor
    def __init__(self, coeficiente=0, exponente=0):
        self.__coeficiente = coeficiente
        self.__exponente = exponente

    @property
    def coeficiente(self):
        return self.__coeficiente

    @property
    def exponente(self):
        return self.__exponente

    @property
    def to_database(self):
        dict = {}
        dict['type'] = "Monomio"
        dict['coeficiente'] = self.__coeficiente
        dict['exponente'] = self.__exponente
        return dict

    def evaluar(self, valor):
        return self.__coeficiente * pow(valor, self.__exponente)

    def __repr__(self):
        return f"{self.__coeficiente} x^{self.__exponente}"
