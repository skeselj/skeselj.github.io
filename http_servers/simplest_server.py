import http.server
import socketserver

PORT = 8080

# I want to override this class to use my own do_GET function.
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()