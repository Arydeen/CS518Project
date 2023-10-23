import unittest
import pymongo
import sys
mycol = None

def initialize():
    global mycol
    
    my_client = pymongo.MongoClient("mongodb+srv://kgoodwin109:groupgpass@groupg.bzdklql.mongodb.net/?retryWrites=true&w=majority", serverSelectionTimeoutMS=5000)

    try:
        my_client.server_info()
    except pymongo.errors.ServerSelectionTimeoutError as err:
        print("Connection timed out, please check if your mongod is running!")
        sys.exit(1)

    my_database = my_client["mydatabase"]
    mycol = my_database['mycollection']

def reset():
    global mycol
    mycol.drop
    mycol = None

def create(document):

    try:
        mycol.insert_many(document)
        return True
    except:
        return False

def read(query, one=False):

    if(one == True):
        return mycol.find(query)[0]
    else:
        return mycol.find(query)

def update(query, new_values):

    try:
        mycol.update_many(query, {"$set": new_values})
        return True
    except:
        return False

def delete(query):

    try:
        mycol.delete_many(query)
        return True
    except:
        return False



if __name__ == "__main__":

    create([{'title':'test','message':"testing 1 2"}])
    initialize()

    print("testing create / read one")
    create([{'title':'test','message':"testing 1 2"}])
    create([{'title':'test1','message':"different message"}])
    create([{'title':'test','message':"testing 10 20"}])

    doc = read({}, one=True)
    print(doc)

    print("\ntesting read all")
    doc = read({})
    for i in doc:
        print(i)

    print("\ntesting update")
    update({'title':'test'}, {'message':"testing 3 4"})
    doc = read({}, one=True)
    print(doc)

    print("\ntesting delete")
    delete({'title':'test'})
    doc = read({})
    for i in doc:
        print(i)

    reset()

