''' Serve over an HTTPS connection, with a self-signed certificate.'''

import http.server
import ssl
import socket
import socketserver

PORT = 4443

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
    # Debug information.
    host_name = socket.gethostname()
    IP = socket.gethostbyname(host_name)
    print(f'host_name = {host_name:}, IP = {IP:}, PORT = {PORT:}')

    # The certificate is "self-signed", which chrome doesn't like too much.
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                   server_side=True,
                                   keyfile='localhost.key',
                                   certfile='localhost.crt')

    httpd.serve_forever()


