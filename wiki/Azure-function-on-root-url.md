# Serving Content at Root URL in Azure Functions for LivelyGraph

## Objective
Configure Azure Functions (V4 and backward compatible with V3) to serve content from the root URL (`/`).

## Background
- In Azure Functions V4, proxies were disabled and then re-enabled but are still deprecated.
- Microsoft recommends Azure API Management for complex routing, but for simpler cases, the following method is effective.

## Steps

### 1. Disable Azure Functions Default Homepage
To prevent Azure Functions from serving its default homepage, set `AzureWebJobsDisableHomepage` to `true`.

- **In Azure**:
  - Go to Azure Functions Application Settings and add this setting.

- **Locally**:
  - Add the setting to `local.settings.json`:
    ```json
    {
      "IsEncrypted": false,
      "Values": {
        "AzureWebJobsDisableHomepage": "true"
      }
    }
    ```

### 2. Remove Default "/api" Prefix
Update `host.json` to remove the default "/api" route prefix.

- Modify `host.json` as follows:
  ```json
  {
    "version": "2.0",
    "extensions": {
      "http": {
        "routePrefix": ""
      }
    }
  }
  ```

### 3. Create a Function with Root Route
Define a function with `Route = "/"` to serve custom content or perform actions.

- **Example (Python Azure Function)**:
  ```python
  import azure.functions as func

  def main(req: func.HttpRequest) -> func.HttpResponse:
      # Custom logic here
      return func.HttpResponse("Welcome to LivelyGraph!", status_code=200)
  ```

## Considerations
- This setup allows serving custom content or performing actions directly at the root URL.
- Use this method cautiously to avoid routing conflicts, especially in apps with multiple functions.

## Acknowledgment
- This solution is adapted from https://stackoverflow.com/a/76419027.
  
## Applicability
- This method is suitable for Azure Functions V4 and is backward compatible with V3.
