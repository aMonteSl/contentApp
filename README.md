# Clase contentApp

Repositorio de plantilla para el ejercicio "Clase contentAPP". Recuerda que puedes consultar su enunciado en la guía de estudio (programa) de la asignatura.


# Simple Web Server

This is a simple web server implemented in Python. It serves HTML content based on the requested resource.

## Usage

1. Clone the repository: git clone https://github.com/your_username/your_repository.git


2. Navigate to the project directory: cd your_repository


3. Run the server: python3 server.py


4. Open your web browser and go to `http://localhost:1234` to access the web server (DEFAULT PORT: 1234).

## Features

- Handles HTTP GET requests.
- Serves HTML content based on requested resources.
- Supports basic error handling (404 Not Found).

## Customization

You can customize the server by modifying the `resources` dictionary in the `WebNames` class. Each key-value pair represents a resource name and its corresponding HTML content.

```python
class WebNames(WebApp):
    """A web application that handles names."""

    def __init__(self, hostname, port):
        resources = {
            "David": "<html><body>Hello, I'm David</body></html>",
            "Pedro": "<html><body>Hello, I'm Pedro</body></html>",
            "Juan": "<html><body>Hello, I'm Juan</body></html>",
            "María": "<html><body>Hello, I'm María</body></html>",
            "Luis": "<html><body>Hello, I'm Luis</body></html>"
        }
        super().__init__(hostname, port, resources)
```

