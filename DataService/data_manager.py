import pymongo
import unittest
from bson import ObjectId
import json

"""
This is a reST style.

:param param_1: this is the first parameter
:param param_2: this is the second parameter
:returns: this is a description of what is returned
:raises keyError: raises an exception

"""

# use a global variable to store your collection object
mycol = None

"""
Connect to the local MongoDB server, database, and collection.

"""


def initialize():
    # specify that we are using the global variable mycol
    global mycol

    #########################
    # INSERT YOU CODE BELOW #
    #########################

auth_str = "arydeen:Dk1NwOtjKVYCWcxH"
# URL will be something like your_username.combination_of_nums_letters.mongodb.net
conn_url = "groupgcluster.e8wuxq3.mongodb.net/?retryWrites=true&w=majority"
conn_str = f"mongodb+srv://{auth_str}@{conn_url}"
# use the conn_str to connect to your MongoDB Atlas cluster
client = pymongo.MongoClient(conn_str)

# client = pymongo.MongoClient("mongodb+srv://arydeen:<Dk1NwOtjKVYCWcxH>@groupgcluster.e8wuxq3.mongodb.net/?retryWrites=true&w=majority")
myDB = client["manDB"]
mycol = myDB["manCol"]


"""
Drop the collection and reset global variable mycol to None.

"""


def reset():
    # specify that we are using the global variable mycol
    global mycol

    #########################
    # INSERT YOU CODE BELOW #
    #########################

    mycol.drop()
    mycol = None


"""
Insert document(s) into the collection.

:param document: a Python list of the document(s) to insert
:returns: result of the operation

"""


def create(document):
    #########################
    # INSERT YOU CODE BELOW #
    #########################
    mycol.insert_one(document)


"""
Retrieve document(s) from the collection that match the query,
if parameter one is True, retrieve the first matched document,
else retrieve all matched documents.

:param query: a Python dictionary for the query
:param one: an indicator of how many matched documents to be retrieved, by default its value is False
:returns: all matched document(s)

"""


def json_encoder(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    raise TypeError("Type not serializable")

def read(query, one=False):
    #########################
    # INSERT YOUR CODE BELOW #
    #########################

    if one:
        result = mycol.find_one(query)
        if result:
            return json.dumps(result, default=json_encoder)
        else:
            return None
    else:
        results = mycol.find(query)
        return json.dumps(list(results), default=json_encoder)
    
# def read(query, one=False):

#     if(one == True):
#         return list(mycol.find(query)[0])
#     else:
#         return list(mycol.find(query))


"""
Update document(s) that match the query in the collection with new values.

:param query: a Python dictionary for the query
:param new_values: a Python dictionary with updated data fields / values
:returns: result of the operation

"""


def update(query, new_values):
    #########################
    # INSERT YOU CODE BELOW #
    #########################
    mycol.update_many(query, {'$set': new_values})


"""
Remove document(s) from the collection that match the query.

:param query: a Python dictionary for the query
:returns: result of the operation

"""


def delete(query):
    #########################
    # INSERT YOU CODE BELOW #
    #########################
    mycol.delete_many(query)


if __name__ == "__main__":
    # sample tests
    initialize()

    print("testing create / read")
    create([{'title': 'test', 'message': "testing 1 2"}])
    doc = read({}, one=True)
    print(doc)

    print("testing update")
    update({'title': 'test'}, {'message': "testing 3 4"})
    doc = read({}, one=True)
    print(doc)

    print("testing delete")
    delete({'title': 'test'})
    doc = read({})
    print(doc)

    reset()

    #########################
    # INSERT YOU TESTS BELOW #
    #########################

    print("Testing create() before insert() throws attribute exception:")
    try:
        create([{'title': 'test', 'message': "testing 1 2"}])
    except:
        print("Attribute Error Thrown: Cannot create() before initialize()")

    print("Testing Read on document that doesnt exist. Should be None: ")
    initialize()
    create([{'title': 'test', 'message': "testing 1 2"}])
    doc = read({'title': 'null'}, one=True)
    print(doc)

    print("Testing Read on document that doesnt exist: ")
    print(read({'title': 'null'}, one=True))
    delete({'title': 'null'})
    print("Should still be None: ")
    print(read({'title': 'null'}, one=True))

