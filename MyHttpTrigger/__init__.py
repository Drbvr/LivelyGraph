import azure.functions as func
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Assuming the HTML file is in the same directory as the function
        with open(os.path.join(os.getcwd(), 'landing-page.html'), 'r') as file:
            html_content = file.read()

        return func.HttpResponse(html_content, mimetype="text/html")
    except Exception as e:
        return func.HttpResponse(
             f"Error: {str(e)}",
             status_code=500
        )
