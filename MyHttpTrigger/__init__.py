import azure.functions as func
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        html_file_path = os.path.join(script_dir, 'landing-page.html')

        with open(html_file_path, 'r') as file:
            html_content = file.read()

        return func.HttpResponse(html_content, mimetype="text/html")
    except Exception as e:
        return func.HttpResponse(
             f"Error: {str(e)}",
             status_code=500
        )
