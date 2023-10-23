import azure.functions as func
import logging
import data_manager

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

data_manager.initialize()

@app.route(route="CreateRecord")
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
        data_manager.create([indoc])
        return func.HttpResponse(f"Record added.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a document in the query string or in the request body to create a record",
             status_code=200
        )

@app.route(route="ReadRecords")
def ReadRecords(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        doc = data_manager.read('name')
        return func.HttpResponse(doc)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
