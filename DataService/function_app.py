import azure.functions as func
import logging
import data_manager
import json
from bson import json_util

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

data_manager.initialize()

@app.route(route="CreateRecord", methods = ['POST'])
def CreateRecord(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    indoc = req.get_json()
    if not indoc:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            indoc = req_body.get('indoc')
    if indoc:
        data_manager.create(indoc)
        return func.HttpResponse(f"Record added.", status_code=200)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a document in the query string or in the request body to create a record",
             status_code=200
        )
    
@app.route(route="DeleteRecord", methods = ['DELETE'])
def DeleteRecord(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request')
    indoc = req.get_json()
    if not indoc:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            indoc = req_body.get('indoc')
    if indoc:
        data_manager.delete(indoc)
        return func.HttpResponse(f"Record Deleted", status_code=200)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a document in the query string or in the request body to create a record",
             status_code=200
        )
    
# @app.route(route="UpdateRecord", methods = ['PUT'])
# def UpdateRecord(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')
#     indoc = req.get_json()
#     if not indoc:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             indoc = req_body.get('indoc')
#     if indoc:
#         data_manager.update(indoc)
#         return func.HttpResponse(f"Record added.", status_code=200)
#     else:
#         return func.HttpResponse(
#              "This HTTP triggered function executed successfully. Pass a document in the query string or in the request body to create a record",
#              status_code=200
#         )

@app.route(route="ReadRecords", methods = ['GET'])
def ReadRecords(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    print("Inside ReadRecords")
    name = req.params.get('query')
    if not name:
        doc = data_manager.read({})
        return func.HttpResponse(str(doc))

    else:
        doc = data_manager.read(json.loads(name))
        return func.HttpResponse(str(doc))