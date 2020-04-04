import http.server
import socketserver
import socket

# TODO(skeselj): override this.
Handler = http.server.SimpleHTTPRequestHandler

PORT = 8080

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    host_name = socket.gethostname()
    IP = socket.gethostbyname(host_name)

    print(f'Serving at host (IP: {IP:}, name: {host_name:}), port {PORT:}')

    httpd.serve_forever()