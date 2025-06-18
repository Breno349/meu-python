from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = self.path

        if path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Olá, mundo!".encode('utf-8'))

        elif path == "/json":
            data = {"mensagem": "Isso é um JSON!", "status": "ok"}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif path == "/html":
            html = "<html><body><h1>Página HTML</h1></body></html>"
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Rota não encontrada".encode('utf-8'))

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, handler)
    print("Servidor rodando em http://localhost:8000")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
