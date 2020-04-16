''' Serve over an HTTPS connection, with a self-signed certificate.

This won't work over Chrome, but it does work with "$ curl -k".
'''

import http.server
import ssl
import socket
import socketserver

PORT = 4443

# Without the 'ssl.wrap_socket' line, this works.
with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    # Debug information.
    host_name = socket.gethostname()
    IP = socket.gethostbyname(host_name)
    print(f'host_name = {host_name:}, IP = {IP:}, PORT = {PORT:}')

    # The certificate is "self-signed", which chrome doesn't like too much.
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                   server_side=True,
                                   keyfile='ssl/localhost.key',
                                   certfile='ssl/localhost.crt')

    httpd.serve_forever()


