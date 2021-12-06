import pymongo
from pprint import pprint
from Monomio import Monomio
from Polinomio import Polinomio
from Expresion import Expresion
from vars import *

if __name__ == '__main__':
    client = pymongo.MongoClient(URL)
    db = client[DB_NAME]

    print('''
    #   Consultar e imprimir la cantidad total de expresiones, de polinomios y de monomios almacenados
    #       como documentos
    ''')
    pprint(db.algebra.count_documents({}))

    print('''
    #   Consultar e imprimir el monomio con potencia 7 de los primeros 10 polinomios que tengan grado 7 y
    #       que estén guardados como documentos.
    ''')
    pprint(list(
        db.algebra.find({
            'type': 'Polinomio', 
            'grado':7,
            'monomios': {
                '$elemMatch': {
                    'exponente': 7
                }
            }
        }, limit=10)
    ))

    print(''')
    # Consultar e imprimir la cantidad total de expresiones que tengan polinomios como ambos operandos.
    ''')
    pprint(
        db.algebra.count_documents({
            'type': 'Expresion', 
            'operando1.type': 'Polinomio',
            'operando2.type': 'Polinomio'
        })
    )

    print('''
    #   Consultar e imprimir las primeras 7 expresiones cuyo primer operando sea un monomio, la impresión
    #       debe ser operando1 operador operando2.
    ''')
    results = db.algebra.find({
        'type': 'Expresion', 
        'operando1.type': 'Monomio',
    }, limit=7)

    for result in results:
        val1 = Monomio(
            result['operando1']['coeficiente'],
            result['operando1']['exponente']
        ) 

        val2 = None
        if result['operando2']['type'] == 'Polinomio':
            val2 = Polinomio()
            for monomio in result['operando2']['monomios']:
                monomio_obj = Monomio(
                    monomio['coeficiente'],
                    monomio['exponente']
                ) 
                val2.agregar(monomio_obj)
        else:
            val2 = Monomio(
                result['operando2']['coeficiente'],
                result['operando2']['exponente']
            ) 
        print(Expresion(result['operacion'], val1, val2))

    print('''
    #   Consultar e imprimir los 2 primeros monomios de cada uno de los primeros 25 polinomios que tengan
    #       3 o más monomios.
    ''')
    results = db.algebra.find({
        'type': 'Polinomio', 
        'length': {
            '$gte': 3
        }
    }, limit=25)
    for polinomio in results:
        pprint({
            '_id': polinomio['_id'],
            'monomio 0': polinomio['monomios'][0],
            'monomio 1': polinomio['monomios'][1]
        })

    print('''
    #   Consultar e imprimir la cantidad total de monomios en la base de datos, independientemente de que
    #       estén como documentos, como parte de un polinomio o de una expresión.
    ''')
    count = db.algebra.count_documents({'type':'Monomio'})

    results = db.algebra.find({
        '$or': [
            {'type': 'Polinomio'},
            {'type': 'Expresion'}
        ]
    })

    for element in results:
        if element['type'] == 'Polinomio': count += element['length']
        else:
            for operando in [element['operando1'], element['operando2']]:
                if operando['type'] == 'Monomio': count += 1
                else: count += operando['length']
    print(count)