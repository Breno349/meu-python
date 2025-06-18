from http.server import BaseHTTPRequestHandler
 
class handler(BaseHTTPRequestHandler):
 
"""def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return"""

def handler(request, response):
    # Cabeçalhos customizados
    response.set_header('Content-Type', 'text/plain; charset=utf-8')
    response.set_header('X-Custom-Header', 'MeuServidorVercel')

    # Acessando o método HTTP
    method = request.method

    # Pegando caminho e query params
    path = request.url
    query = request.args  # dict-like com parâmetros da query string

    # Criando resposta baseada no método
    if method == 'GET':
        # Exemplo de resposta simples
        response.status_code = 200
        name = query.get('name', 'mundo')
        response.send(f"Olá, {name}! Você acessou: {path}\nMétodo: {method}\n")
    else:
        # Métodos não implementados
        response.status_code = 405
        response.set_header('Allow', 'GET')
        response.send("Método não permitido")
