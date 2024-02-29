#!/usr/bin/python3
import socket

class WebApp:
    """A basic web application."""

    def __init__(self, hostname, port, resources):
        """Initialize the web application."""
        self.hostname = hostname
        self.port = port
        self.resources = resources

        # Start the server
        self.start_server()

    def start_server(self):
        """Start the server."""
        # AF_INET = IPv4, SOCK_STREAM = TCP
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Enable address reuse
        my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind the socket to an address and port
        my_socket.bind((self.hostname, self.port))

        # Maximum queue of 5 TCP connections
        my_socket.listen(5)

        while True:
            print("Waiting for a connection...")
            connection_socket, addr = my_socket.accept()
            print(f"Connection received from: {addr}")
            received = connection_socket.recv(2048)
            print(f"Raw bytes received: {received}\n\n")

            # Handle/parse resources
            parsed_request = self.parse(received.decode("utf-8"))
            
            # Process the request and create the response
            return_code, html_response = self.process(parsed_request)

            # Send response
            response = f"HTTP/1.1 {return_code}\r\n\r\n{html_response}\r\n"
            connection_socket.send(response.encode("utf-8"))
            connection_socket.close()

    def parse(self, request):
        """Parse the request extracting the information."""
        resource = request.split()[1][1:]  # Extract the resource name without the initial slash

        return resource
    
    def process(self, parsed_request):
        """Process the request data."""
        if parsed_request.lower() in self.resources:
            return "200 OK", self.resources[parsed_request.lower()]
        else:
            if parsed_request == "":
                all_resources = "<br>".join(self.resources.keys())
                return "200 OK", f"<html><body>Possible resources:<br>{all_resources}</body></html>"
            else:
                return "404 Not Found", "<html><body>Error 404: Resource not found</body></html>"


class WebNames(WebApp):
    """A web application that handles names."""

    def __init__(self, hostname, port):
        resources = {
            "david": "<html><body>Hello, I'm David</body></html>",
            "pedro": "<html><body>Hello, I'm Pedro</body></html>",
            "juan": "<html><body>Hello, I'm Juan</body></html>",
            "maria": "<html><body>Hello, I'm Maria</body></html>",
            "luis": "<html><body>Hello, I'm Luis</body></html>",
            "adrian": "<html><body>Hello, I'm Adrian and I am the admin/author of this server</body></html>"
        }
        super().__init__(hostname, port, resources)


if __name__ == "__main__":
    my_webapp = WebNames("", 1234)


