import os
from http.server import BaseHTTPRequestHandler, HTTPServer

MESSAGE = os.environ.get("MESSAGE", "Bonjour depuis le conteneur")

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write((MESSAGE + "\n").encode())

HTTPServer(("0.0.0.0", 8000), H).serve_forever()
# test
