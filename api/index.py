from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return

def run():
    server_address = ('', 80)
    httpd = HTTPServer(server_address, handler)
    print("Servidor rodando na porta 80...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
