import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # You can access query parameters using req.params.get('parameterName')
    # or POST data using req.get_json()

    return func.HttpResponse("This is a response from your Azure Function!", status_code=200)
