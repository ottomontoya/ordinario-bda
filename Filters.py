import pymongo
import pprint
import bson.objectid


class Filters:

    def ExpGte650(self):
        # Conect to the Atlas UI Cluster
        client = pymongo.MongoClient(
            "mongodb+srv://analytics:analytics-password@mflix.wti8n.mongodb.net/myFirstDatabase?ssl=true&ssl_cert_reqs=CERT_NONE")
        db = client.bda.algebraTest
        # Query 1 - Todos los monomios y polinomios que tengan un exponnete mayor a 650,

        # Query
        query1 = {"$and": [{"$or": [{"type": "Polinomio"}, {"type": "Monomio"}]},
                           {"$or": [{"exponente": {"$gte": 650}}, {"monomios.exponente": {"$gte": 650}}]}]}

        # Projection
        projection1 = {"_id": 0, "type": 1, "exponente": 1,
                       "coeficiente": 1, "monomios": 1}

        # count
        print(db.find(query1, projection1).count())
        # print all of the trips
        for doc in db.find(query1, projection1):
            pprint.pprint(doc)

    def PoliCoefGte100Lte400(self):
        # Conect to the Atlas UI Cluster
        client = pymongo.MongoClient(
            "mongodb+srv://analytics:analytics-password@mflix.wti8n.mongodb.net/myFirstDatabase?ssl=true&ssl_cert_reqs=CERT_NONE")
        db = client.bda.algebraTest
        # Query 1 - Todos los monomios y polinomios que tengan un exponnete mayor a 650,

        # Query
        query = {"type": "Polinomio", "monomios.coeficiente": {
            "$gte": 100, "$lte": 400}}

        # Projection
        projection = {"_id": 0, "type": 1,
                      "monomios.exponente": 1, "monomios.coeficiente": 1}

        # count
        print(db.find(query, projection).count())
        # print all of the trips
        for doc in db.find(query, projection):
            pprint.pprint(doc)

    def TypeMonomioCoefGte400(self):
        # Conect to the Atlas UI Cluster
        client = pymongo.MongoClient(
            "mongodb+srv://analytics:analytics-password@mflix.wti8n.mongodb.net/myFirstDatabase?ssl=true&ssl_cert_reqs=CERT_NONE")
        db = client.bda.algebraTest
        # Query 1 - Todos los monomios y polinomios que tengan un exponnete mayor a 650,

        # Query
        query = {"type": "Monomio", "coeficiente": {
            "$gte": 400}}

        # Projection
        projection = {"_id": 0, "type": 1, "exponente": 1, "coeficiente": 1}

        # count
        print(db.find(query, projection).count())
        # print all of the trips
        for doc in db.find(query, projection):
            pprint.pprint(doc)

    def TypePoliArrayIs5(self):
        # Conect to the Atlas UI Cluster
        client = pymongo.MongoClient(
            "mongodb+srv://analytics:analytics-password@mflix.wti8n.mongodb.net/myFirstDatabase?ssl=true&ssl_cert_reqs=CERT_NONE")
        db = client.bda.algebraTest
        # Query 1 - Todos los monomios y polinomios que tengan un exponnete mayor a 650,

        # Query
        query = {"type": "Polinomio", "monomios": {"$size": 5}}

        # Projection
        projection = {"_id": 0, "type": 1,
                      "monomios.exponente": 1, "monomios.coeficiente": 1}

        # count
        print(db.find(query, projection).count())
        # print all of the trips
        for doc in db.find(query, projection):
            pprint.pprint(doc)
