import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    html_content = "<html><body><h1>Hello from Azure Function!</h1></body></html>"
    return func.HttpResponse(html_content, mimetype="text/html")
