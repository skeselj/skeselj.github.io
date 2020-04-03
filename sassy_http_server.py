import http.server
import socketserver
import socket
import os

# class SassyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header("Content-type", 'text/html')
#         self.end_headers()
#         return
SassyHTTPRequestHandler = http.server.SimpleHTTPRequestHandler

PORT = 8080
with socketserver.TCPServer(("", PORT), SassyHTTPRequestHandler) as httpd:
    host_name = socket.gethostname()
    IP = socket.gethostbyname(host_name)

    print(f'Serving at host (IP: {IP:}, name: {host_name:}), port {PORT:}')

    httpd.serve_forever()