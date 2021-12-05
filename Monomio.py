class Monomio:

    # Constructor
    def __init__(self, coeficiente=0, exponente=0):
        if coeficiente < 0:
            raise Exception('El coeficiente no debe ser negativo')
        elif exponente < 0:
            raise Exception('El exponente no debe ser negativo')
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
        obj = dict()
        obj['type'] = "Monomio"
        obj['coeficiente'] = self.__coeficiente
        obj['exponente'] = self.__exponente
        return obj

    def evaluar(self, valor):
        return self.__coeficiente * (valor ** self.__exponent)

    def sumar(self, monomio):
        return self + monomio
    
    def restar(self, monomio):
        return self - monomio

    # Dunder methods
    def __repr__(self):
        '''Representación'''
        return f"{self.__coeficiente} x^{self.__exponente}"

    def __add__(self, value):
        '''Habilitar y definir operador suma'''
        if not isinstance(value, Monomio) or self.__exponente != value.__exponente:
            raise Exception('Una instancia de Monomio solo puede operar con otro Monomio con el mismo exponente')
        return Monomio(self.__coeficiente + value.__coeficiente, self.__exponente)

    def __sub__(self, value):
        '''Habilitar y definir operador substracción'''
        if not isinstance(value, Monomio) or self.__exponente != value.__exponente:
            raise Exception('Una instancia de Monomio solo puede operar con otro Monomio con el mismo exponente')
        return Monomio(self.__coeficiente - value.__coeficiente, self.exponente)